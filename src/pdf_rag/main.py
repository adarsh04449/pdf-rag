#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from pdf_rag.crew import PdfRag

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """

    user_input = input("Enter your question: ")
    inputs = {
        "input" : user_input
    }
    
    try:
        result = PdfRag().crew().kickoff(inputs=inputs)
        print(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


