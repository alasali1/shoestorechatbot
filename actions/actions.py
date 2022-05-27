from typing import Text, List, Any, Dict
import logging
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_SHOE_SIZES = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
#ALLOWED_SHOE_TYPES = ["jordan", "reebok", "airmax", "vans", "kawhi", "lebron", "converse", "airforce"]


class ValidateSimpleShoeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_shoe_form"

    def validate_shoe_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'shoe_size' value."""

        if slot_value.lower() not in ALLOWED_SHOE_SIZES:
            dispatcher.utter_message(text=f"We only have sizes 1-13")
            return {"shoe_size": None}
        dispatcher.utter_message(text=f"OK! You want a size {slot_value} shoe.")
        return {"shoe_size": slot_value}

    # def validate_shoe_type(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate 'shoe_type' value."""

    #     if slot_value not in ALLOWED_SHOE_TYPES:
    #         dispatcher.utter_message(text=f"We do not have that shoe in stock. We only carry {'/'.join(ALLOWED_SHOE_TYPES)}.")
    #         return {"shoe_type": None}
    #     dispatcher.utter_message(text=f"OK! You want a pair of {slot_value}.")
    #     return {"shoe_type": slot_value}

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

