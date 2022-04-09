import module
import view
import logger 

def button_click():
    result = module.do_it()
    view.view_data(result)
    logger.html_logger(result)

