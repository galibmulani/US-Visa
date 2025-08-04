import os
import sys

def error_message_detail(error_message,error_detail:sys):
    _,_,exc_table = error_detail.exc_info()
    file_name = exc_table.tb_frame.f_code.co_filename
    
    error_message = "Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_table.tb_lineno,str(error_message)
        )
    return error_message;

class USVisaException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message=error_message,
            error_detail=error_detail
        )

    def __str__(self):
        return self.error_message;