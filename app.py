from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st


class AppModel:
  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
# Tell the tokenizer to use the EOS token for padding
    self.tokenizer.pad_token = self.tokenizer.eos_token
    self.model= AutoModelForCausalLM.from_pretrained("./output/model/checkpoint-2740")

  def generate_plot(self, prompt: str):

    #prompt = "A short film about a pilot who"
#Tokenize the prompt (this now creates an accurate attention_mask)
    inputs = self.tokenizer(prompt,return_tensors="pt").to("cpu")

# Pass **inputs (unpacks both input_ids AND attention_mask) 
# and explicitly set the pad_token_id
    outputs = self.model.generate(# type: ignore
  #inputs.input_ids,
    **inputs,
    max_new_tokens=100,
    do_sample=True,
    top_k=50,
    top_p=.95,
    pad_token_id=self.tokenizer.eos_token_id
   )

    #output_string=self.tokenizer.batch_decode(outputs)
    output_string = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    return output_string
  
@st.cache_resource
def load_app_model():
  return AppModel()

  # Initialize the cached model singleton
model = load_app_model()

# 3. Build the Streamlit User Interface
st.title("🎬 AI Script & Plot Generator")

prompt = st.text_input("Enter the beginning of your plot ...")
clicked = st.button("Generate my plot!")

# 4. Handle the button click and render the outputs to the UI
if clicked:
    if prompt.strip() == "":
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("AI is thinking and writing your plot on the CPU..."):
            # Call the generation function
            generated_script = model.generate_plot(prompt)
            
            # Print the final result back to the user interface
            st.subheader("Generated Plot:")
            st.write(generated_script)
