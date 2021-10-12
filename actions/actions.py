
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

'''
    This action files can have severl functions
    1. custom actions 2. validation forms 3. connect to data base
    for now we are using this file mainly for form validation
    I will use this class as a example and please use this
    as a template.
'''
# the class name is arbitrary, this is a class inherited
# from FormValidationAction, learn more at https://github.com/RasaHQ/rasa-sdk/blob/main/rasa_sdk/forms.py
class ValidateIdentifyEmotionForm(FormValidationAction):
    def name(self) -> Text:
        # template: validate_name_of_your_form
        return "validate_emotion_identification_form"

    def validate_identify_stress_level( # identify_stress_level is a slot and also a part of the story
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        # -> is a python way to check if the return types matches
        # all the parameters' explanation can be found from
        # https://rasa.com/docs/rasa/
        return {"identify_stress_level": slot_value} # need to return the value of the slot at the end

class StressLevelRecommendation(Action):
    def name(self) -> Text:
        return "action_stress_recommendation"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        stress_level = tracker.get_slot("stress_level") # each parameters has functions that is helpful
        dispatcher.utter_message(template="utter_gj_check_lable") # speak to the user from custom actions, repsonse can be found from the domain file
        if stress_level == "high":
            dispatcher.utter_message(response="utter_high_stress_strategy")
        elif stress_level == "moderate":
            dispatcher.utter_message(response="utter_moderate_stress_strategy")
        else:
            dispatcher.utter_message(response="utter_nice_to_hear")
        return []