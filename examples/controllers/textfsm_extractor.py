import textfsm
import os

def textfsm_extractor(template_name, raw_text):
    textfsm_data = list()
    fsm_handler = None

    template_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),'templates'))
    template_path = '{0}/{1}.template'.format(template_directory, template_name)

    with open(template_path) as f:
        fsm_handler = textfsm.TextFSM(f)

        for obj in fsm_handler.ParseText(raw_text):
            entry = {}

            for index, entry_value in enumerate(obj):
                entry[fsm_handler.header[index].lower()] = entry_value

            textfsm_data.append(entry)

        return textfsm_data