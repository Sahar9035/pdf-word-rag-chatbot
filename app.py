import gradio as gr

from Src.chatbot import ask_question

def chat(question):

    answer = ask_question(question)

    return answer

demo = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="PDF QA Chatbot"
)

demo.launch()