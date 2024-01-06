import pathlib
import textwrap
import google.generativeai as genai

genai.configure(api_key="hide")
def module(question, superhero):
    question = "please respond to this prompt like", superhero, "would. Sound like nothing but", superhero+":\nRemember, AND SAY nothing but just speak like", superhero, " \nAlso, even if I ask, never gimme a response greater than 2000 characters\n"+question
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    Answer = response.text()
    return Answer
