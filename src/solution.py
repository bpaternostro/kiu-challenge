import os

from datetime import datetime

class PackageController():
    VALID_FORMATS = ["txt"]

    def __init__(self, p_date:str, input_file:str, rate:float) -> None:
        """
            params: 
                (str) p_date --> proccesing date
                (str) input_file --> file to be processed
                (float) rate --> rate by order
        """
        self.p_date = p_date
        self.input_file = input_file
        self.rate = rate
        self.sub_totals = []
        self.total = None

    def _check_file_format(self, file_name) -> bool:
        if not (file_name.split(".")[-1] in self.VALID_FORMATS):
            raise Exception(f"Input file extension is not supported. Valid formats: {self.VALID_FORMATS}") 
    
    def _normalize_values(self, p_str) -> str:
        """
            method to replace \n in columns and rows
            params: (str) p_str --> string to be processed

            return: (str) normalized
        """
        return p_str.replace("\n", "")
    
    def _get_data_from_input(self) -> list:
        """
            get all the data from input_file and parse into a dictionary
            param: N/A
            return : (list) of dictionaries    
        """
        try:
            self._check_file_format(self.input_file)
            
            with open(self.input_file, 'r') as f:
                all_lines = f.readlines()
                header = [self._normalize_values(col) for col in all_lines[0].split("|")] #this is to normalize cols names 
                return [{header[index]:p for index,p in enumerate(l.split("|"))} for l in all_lines[1:]] 
        except Exception as e:
            raise Exception(f"Problems opening the file {self.input_file}. The error was:{e}")

    def generate_total_report(self) -> list:
        """ 
            this method generates a report in ./ with all the proceced data for p_date param
            params: 
                (str): p_date -> filter date, must be in yyyy-mm-dd format
                (str): output_name -> file's name with the result for a given date

            return: (bool)
        """
        def _check_date(timestamp:str)-> bool: # compare the order date against the input parameter
            datetime_from_file = datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d")
            return self.p_date == datetime_from_file
        
        def _calculate_subtotal(p): # by row
            calc = int(p.get("quantity")) * float(self.rate)
            self.sub_totals.append(calc)
            p["subtotal"] = calc
            return p

        try:
            data_from_date = list(filter(lambda p: _check_date(p.get("timestamp")), self._get_data_from_input()))
            process_sub_total = list(map(lambda p: _calculate_subtotal(p), data_from_date))
            self.total = sum(self.sub_totals)
            return process_sub_total
        except Exception as e:
            raise Exception(f"There were problems executing generate_total_report method. Error: {e}")
        

    def export_results(self, data_to_be_exported:list, output_name:str) -> bool:
        
        self._check_file_format(output_name)
            
        if not (len(data_to_be_exported)):
            return False
        
        try:
            with open(output_name, 'w') as f:
                columns = list(data_to_be_exported[0].keys())
                f.write(f"#Total report generated for date {self.p_date}.\n")
                f.write(f"#The rate by order is {float(self.rate)}.\n\n")
                f.write(' | '.join(columns))
                f.write('\n')
                for l in data_to_be_exported:
                    f.write(f"{l.get('order_id')} | {l.get('origin')} | {l.get('destiny')} | {l.get('timestamp')} | {self._normalize_values(l.get('quantity'))} | {l.get('subtotal')}")
                    f.write('\n')
                
                f.write('\n')    
                
                f.write(f"#Total at {self.p_date}: $ {float(self.total)}")
                
            return True
        except Exception as e:
            raise Exception("Problems creating the report {output_name}. The error was:{e}")

###############################################################################################################
input_file = os.getenv("INPUT_FILE")
output_name = os.getenv("OUTPUT_FILE")
processing_date = os.getenv("PROCESSING_DATE")
rate = os.getenv("RATE")
pc = PackageController(p_date=processing_date, input_file = input_file, rate=rate)

try:
    report = pc.generate_total_report()
    result = pc.export_results(data_to_be_exported=report, output_name=output_name)
    if result:
        print("Process was executed successfully")
    else:
        print("There is no data to be precessed")
except Exception as e:
    print(e)
