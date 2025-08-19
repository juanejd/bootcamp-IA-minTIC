from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import torch
import gradio as gr

# needed if the model requires access
login()
model_id = "meta-llama/Llama-3.2-1B-Instruct"

# charge pretrained model
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)

# charge model tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# check if gpu is available in the device
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"Usango GPU: {torch.cuda.get_device_name(device)}")
else:
    device = torch.device("cpu")
    print("Usando CPU")

# move model to the device
model = model.to(device)

# response function which manage the conversation

"""
message -> mensaje actual del usuario
history -> historial de la conversacion
system_message -> mensaje del sistema
max_tokens -> numero maximo de tokens para la respuesta
temperature -> nivel de aleatoriedad de la respuesta
top_p -> control del muestreo
"""


def respond(message, history, system_message, max_tokens, temperature, top_p):
    # initialize the conversation with the system message
    messages = [{"role": "system", "content": system_message}]

    # add conversation history
    for val in history:
        if val[0]:
            message.append({"role": "user", "content": val[0]})
        if val[1]:
            message.append({"role": "assistant", "content": val[1]})
    # add new user message
    messages.append({"role": "user", "content": message})

    # convert the conversation in tensors for the model
    input_ids = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt"
    ).to(device)

    # define tokens that indicate the end of the response
    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>"),
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=max_tokens,
        eos_token_id=terminators,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
    )
    # transform the response in a string
    response = ""
    for message in tokenizer.device(
        outputs[0][input_ids.shape[-1] :],  # tomamos solo la respuesta
        skip_apecial_tokens=True,
    ):
        response += message
        yield respond  # yield para que gradio muestr la respuesta progresivamente


# create chatbot interface
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="Tu eres un asistente amigable", label="System Message"),
        gr.Slider(minimum=1, maximum=2048, value=512, label="Max new Tokens"),
        gr.Slider(minimum=0.1, maximum=1, value=0.95, step=0.05, label="temperature"),
        gr.Slider(minimum=0.1, maximum=1, value=0.95, step=0.05, label="top_p"),
    ],
)

if __name__ == "__main__":
    demo.launch()
