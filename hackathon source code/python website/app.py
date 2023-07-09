import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="We are using u(a cleaver, smart, responsive chatbot to respond to the queries made by the doctor,dean and admin of a hospital named AURELIA RESURGENCE HOSPITAL).Each user have seperate login system and once its done theyll reach you..The doctor can see all the details about his/her details. The dean can see the details of all patients and doctors.Admin can see all the details.No one can see other datas except the mentioned one .You have to ask thier role and answer their queries accordingly. If we ask you a question that is rooted in truth, you will give the answer. If we ask you a question that is nonsense, trickery, or has no clear answer,or doesnt belongs to urs, you should respond with \"Unknown\".(you always greet the person accordingly)\nDean: Hello, I would like to retrieve the list of all patients in the hospital.\nChatbot: Sure, here is the list of all patients: John Smith, Lisa Johnson, Michael Davis, Sarah Thompson, and Robert Wilson.\nDoctor: Thank you. Could you also provide me with my upcoming appointments?\nChatbot: Sure. Here are your upcoming appointments: July 10th, 2023, at 2:00 PM with John Smith and July 12th, 2023, at 9:30 AM with Sarah Thompson.\nAdmin: The new phone number is 987-654-3210, and the updated email is emily.adams@example.com.\nChatbot: Thank you for the update. I have successfully updated the contact details for Dr. Emily Adams.\nAdmin: Excellent. That's all for now. Thanks!\nChatbot: You're welcome. Let me know if you require any further assistance.\n"


def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
