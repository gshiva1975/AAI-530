# -*- coding: utf-8 -*-
"""rag-ai-prompt.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10FzZwdQXd4ZdS9y_Xr8pB-JiV8wl-Mlf

## **Install libraries for handling langchain and transformers**
"""

!pip install langchain huggingface_hub transformers
!pip install langchain-community
!pip install matplotlib pandas

"""## **call gpt2 model and pass the prompt and get the output**
### **RAG (Retrieval-Augmented Generation) application for temperature works in two ways**

### If the question exists in the knowledge base → It retrieves the pre-defined answer directly.
### If the question is not in the knowledge base → It calls an LLM (Language Model) to generate a factual response**
"""

#  Provided prompt to gpt2 model
#     "Write a short story about a robot learning to love.",
#    "Explain the theory of relativity in simple terms.",
#    "Generate a poem about the beauty of nature.",


!pip install transformers

from transformers import pipeline

# Initialize the pipeline for text generation
generator = pipeline('text-generation', model='gpt2')  # You can change the model here

# Example prompts
prompts = [
    "Write a short story about a robot learning to love.",
    "Explain the theory of relativity in simple terms.",
    "Generate a poem about the beauty of nature.",
]


# Generate text for each prompt
for prompt in prompts:
    print(f"Prompt: {prompt}")
    generated_text = generator(prompt, max_length=150, num_return_sequences=1) # Adjust max_length and num_return_sequences as needed

    print(f"Generated Text:\n{generated_text[0]['generated_text']}\n")

"""**Output**
**Prompt: Write a short story about a robot learning to love.**
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Generated Text:
Write a short story about a robot learning to love. Start with a small story about a robot learning to love (as I did for about a decade or so). Next, choose one of the robots' names with a few clues. Finally, ask the robot what it is, and be sure to make sure it answers correctly. If the robot is not sure what it is, check for spelling errors and corrections. This approach gives the robot a chance to learn a few things. There are a lot of other reasons to pick up this style of story, but I believe it is one where your mind is quite engaged with the world at large.

**Prompt: Explain the theory of relativity in simple terms.**
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Generated Text:
Explain the theory of relativity in simple terms.

The two sets of facts do not have to be mutually exclusive.

This will also solve the problem of the existence of a separate universe or of two separate universes with different probabilities and types of time. The question is just how many of the same facts do different sets of facts look like by different criteria.

It is a bit of an effort to figure out what you would like to find.

Since the "same" and "different" sets of facts are different, the more information there is about them, the more it helps us to find what we look for. What would that be like if all three facts could contain only the ones we have found thus far about

**Prompt: Generate a poem about the beauty of nature.**
Generated Text:
Generate a poem about the beauty of nature. It will be read by scientists to determine natural variation of human biology, not only for the human species, but for all the worlds. It is an ideal to say that we are like children of nature, and the whole of human nature is the result of the biological process which gives rise to it. It is impossible not to believe that there is much similarity between natural variability that must be explained, and that our unique uniqueness is its underlying reason for existence.

"The world is full of differences. There are different kinds of people, different races, ages, religions, cultures, and ethnicities. Some are different, some people are equally beautiful, others less so. Nature is a wonderful place

# **Create RAG application for temperature - use gpt2**
"""

# rag application for temperature using hugging face

import os
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

# Set your Hugging Face API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize the pipeline for text generation
generator = pipeline('text-generation', model='gpt2')

# Create a LangChain wrapper around the Hugging Face pipeline
llm = HuggingFacePipeline(pipeline=generator)


def rag_application_for_temperature(user_query):
    # Example RAG application for temperature


    # For this example, we will just create a simple knowledge base.
    knowledge_base = {
        "What is the average temperature in London?": "The average temperature in London is around 11°C.",
        "How hot does it get in Death Valley?": "Death Valley can reach temperatures over 50°C."
    }

    if user_query in knowledge_base:
      return knowledge_base[user_query]
    else:
      prompt = f"""Answer the following question using only factual knowledge.
      Question: {user_query}
      """
      response = llm(prompt)
      return response


# Example usage
user_query = "What is the average temperature in London?"
response = rag_application_for_temperature(user_query)
print(f"User Query: {user_query}")
print(f"Response: {response}")


user_query = "How hot does it get in Death Valley?"
response = rag_application_for_temperature(user_query)
print(f"User Query: {user_query}")
print(f"Response: {response}")

"""**Output**

**User Query: What is the average temperature in London?**

Response: The average temperature in London is around 11°C.

**User Query: How hot does it get in Death Valley?**

Response: Death Valley can reach temperatures over 50°C.

# **Write AI Agent**
"""

#  write an ai agent

from transformers import pipeline
import os
from langchain.llms import HuggingFacePipeline

!pip install transformers
!pip install langchain

# Initialize the pipeline for text generation
generator = pipeline('text-generation', model='gpt2')  # You can change the model here

# Example prompts
prompts = [
    "Write a short story about a robot learning to love.",
    "Explain the theory of relativity in simple terms.",
    "Generate a poem about the beauty of nature.",

]


# Generate text for each prompt
for prompt in prompts:
    print(f"Prompt: {prompt}")
    generated_text = generator(prompt, max_length=150, num_return_sequences=1) # Adjust max_length and num_return_sequences as needed

    print(f"Generated Text:\n{generated_text[0]['generated_text']}\n")




# Set your Hugging Face API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize the pipeline for text generation
generator = pipeline('text-generation', model='gpt2')

# Create a LangChain wrapper around the Hugging Face pipeline
llm = HuggingFacePipeline(pipeline=generator)


def rag_application_for_temperature(user_query):


    # For this example, we will just create a simple knowledge base.
    knowledge_base = {
        "What is the average temperature in London?": "The average temperature in London is around 11°C.",
        "How hot does it get in Death Valley?": "Death Valley can reach temperatures over 50°C."
    }

    if user_query in knowledge_base:
      return knowledge_base[user_query]
    else:
      prompt = f"""Answer the following question using only factual knowledge.
      Question: {user_query}
      """
      # The output of llm(prompt) is a string, so return it directly.
      response = llm(prompt)
      return response

# Example usage
user_query = "What is the average temperature in London?"
response = rag_application_for_temperature(user_query)
print(f"User Query: {user_query}")
print(f"Response: {response}")


user_query = "How hot does it get in Death Valley?"
response = rag_application_for_temperature(user_query)
print(f"User Query: {user_query}")
print(f"Response: {response}")

"""# **Create Prompt dynamically, integrated with temperature analysis**"""

from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import matplotlib.pyplot as plt
import re  # Import the regular expression module
from langchain.memory import ConversationBufferMemory
import pandas as pd
from IPython.display import display
from transformers import pipeline

# Install necessary libraries
!pip install langchain huggingface_hub transformers
!pip install langchain-community matplotlib pandas

# Replace with your Hugging Face Hub API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize the Hugging Face Hub LLM with adjustable temperature
temperature_param = 0.7  # You can change this value

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": temperature_param, "max_length": 64},
    task="text-generation",
)

# Initialize the memory
memory = ConversationBufferMemory(memory_key="chat_history", input_key="combined_input")

def predict_temperature(city, dates_values, user_prompt):
    data_string = "\n".join(
        [f"{item['date']}: {item['value']}°F" for item in dates_values]
    )
    combined_input = f"City: {city}, Date: 2024-01-06, Data: {data_string}"
    full_prompt = f"{user_prompt}\n\n{combined_input}"
    prompt_template = PromptTemplate(
        input_variables=["combined_input"], template="{combined_input}"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)
    prediction = chain.run(combined_input=full_prompt)
    print(f"Prediction for {city}: {prediction}")
    return prediction

def extract_temperature(prediction):
    match = re.search(r"(\d+)", prediction)
    if match:
        return int(match.group(1))
    return None

# Example cities data
cities_data = {
    "Cupertino": [
        {"date": "2024-01-01", "value": 55},
        {"date": "2024-01-02", "value": 58},
        {"date": "2024-01-03", "value": 60},
        {"date": "2024-01-04", "value": 57},
        {"date": "2024-01-05", "value": 62},
    ],
    "San Francisco": [
        {"date": "2024-01-01", "value": 52},
        {"date": "2024-01-02", "value": 55},
        {"date": "2024-01-03", "value": 57},
        {"date": "2024-01-04", "value": 54},
        {"date": "2024-01-05", "value": 59},
    ],
    "Mountain View": [
        {"date": "2024-01-01", "value": 53},
        {"date": "2024-01-02", "value": 56},
        {"date": "2024-01-03", "value": 59},
        {"date": "2024-01-04", "value": 56},
        {"date": "2024-01-05", "value": 61},
    ],
}

# Get user prompt
user_prompt = input("Enter your prompt for time-series analysis: ")

temperatures = {}
for city, data in cities_data.items():
    prediction = predict_temperature(city, data, user_prompt)
    temperatures[city] = extract_temperature(prediction)

cities = [city for city, temp in temperatures.items() if temp is not None]
temps = [temp for temp in temperatures.values() if temp is not None]

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(cities, temps, color="skyblue")
plt.xlabel("City")
plt.ylabel("Predicted Temperature (°F)")
plt.title("LLM Predicted Temperatures for 2024-01-06")
plt.show()

# Display results in a DataFrame
df_results = pd.DataFrame(
    list(temperatures.items()), columns=["City", "Predicted Temperature"]
)
display(df_results)

# Load the text-generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

# Define a prompt
prompt = "Once upon a time in a futuristic city,"

# Generate text
result = generator(prompt, max_length=50, num_return_sequences=1)

# Print the generated text
print("ouptut", result[0]["generated_text"])


# Enhanced temperature prediction using Gen AI with context and analysis
def predict_temperature_enhanced(city, dates_values, user_prompt):
    data_string = "\n".join(
        [f"{item['date']}: {item['value']}°F" for item in dates_values]
    )
    combined_input = f"City: {city}, Date: 2024-01-06, Data: {data_string}"
    historical_trend = "The historical temperature data for the past five days indicates an overall increasing trend."
    enhanced_prompt = (
        f"{user_prompt}\n\nHistorical Trend: {historical_trend}\n\n{combined_input}"
    )
    prompt_template = PromptTemplate(
        input_variables=["combined_input"], template="{combined_input}"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)
    prediction = chain.run(combined_input=enhanced_prompt)
    print(f"Prediction for {city}: {prediction}")
    return prediction

# Example of using Gen AI for text generation with temperature influence
def generate_weather_story(city, temperature):
  prompt = f"Write a short story about a day in {city} where the temperature is {temperature}°F."
  result = generator(prompt, max_length=100, num_return_sequences=1)
  return result[0]["generated_text"]

# Example usage with enhanced prediction and story generation:
temperatures = {}
for city, data in cities_data.items():
    prediction = predict_temperature_enhanced(city, data, user_prompt)
    temperatures[city] = extract_temperature(prediction)

for city, temp in temperatures.items():
    story = generate_weather_story(city, temp)
    print(f"\nWeather story for {city}:\n{story}")

"""# **Use sentence transformer and get cos_similary**"""

# give huggingFaceEmbeddings

!pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util

# Load the Sentence Transformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Example sentences
sentences = [
    "This is an example sentence",
    "Each sentence is converted into an embedding",
    "Sentences are passed as a list of string.",
    "The quick brown rabbit jumps over the lazy frogs.",
]

# Compute embeddings
embeddings = model.encode(sentences)

# Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings, embeddings)

# Print the similarity matrix
cos_sim

"""# **Use LLM to create a story about cites and its tempeature dynamically**"""

# Query

from transformers import pipeline
import os
from langchain.llms import HuggingFacePipeline
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import matplotlib.pyplot as plt
import re  # Import the regular expression module
from langchain.memory import ConversationBufferMemory
import pandas as pd
from IPython.display import display
from sentence_transformers import SentenceTransformer, util

# Install necessary libraries
!pip install transformers langchain huggingface_hub sentence-transformers langchain-community matplotlib pandas

# Replace with your Hugging Face Hub API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize the Hugging Face Hub LLM with adjustable temperature
temperature_param = 0.7  # You can change this value

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": temperature_param, "max_length": 64},
    task="text-generation",
)

# Initialize the memory
memory = ConversationBufferMemory(memory_key="chat_history", input_key="combined_input")

def predict_temperature(city, dates_values, user_prompt):
    data_string = "\n".join(
        [f"{item['date']}: {item['value']}°F" for item in dates_values]
    )
    combined_input = f"City: {city}, Date: 2024-01-06, Data: {data_string}"
    full_prompt = f"{user_prompt}\n\n{combined_input}"
    prompt_template = PromptTemplate(
        input_variables=["combined_input"], template="{combined_input}"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)
    prediction = chain.run(combined_input=full_prompt)
    print(f"Prediction for {city}: {prediction}")
    return prediction

def extract_temperature(prediction):
    match = re.search(r"(\d+)", prediction)
    if match:
        return int(match.group(1))
    return None

# Example cities data
cities_data = {
    "Cupertino": [
        {"date": "2024-01-01", "value": 55},
        {"date": "2024-01-02", "value": 58},
        {"date": "2024-01-03", "value": 60},
        {"date": "2024-01-04", "value": 57},
        {"date": "2024-01-05", "value": 62},
    ],
    "San Francisco": [
        {"date": "2024-01-01", "value": 52},
        {"date": "2024-01-02", "value": 55},
        {"date": "2024-01-03", "value": 57},
        {"date": "2024-01-04", "value": 54},
        {"date": "2024-01-05", "value": 59},
    ],
    "Mountain View": [
        {"date": "2024-01-01", "value": 53},
        {"date": "2024-01-02", "value": 56},
        {"date": "2024-01-03", "value": 59},
        {"date": "2024-01-04", "value": 56},
        {"date": "2024-01-05", "value": 61},
    ],
}

# Get user prompt
user_prompt = input("Enter your prompt for time-series analysis: ")

temperatures = {}
for city, data in cities_data.items():
    prediction = predict_temperature(city, data, user_prompt)
    temperatures[city] = extract_temperature(prediction)

cities = [city for city, temp in temperatures.items() if temp is not None]
temps = [temp for temp in temperatures.values() if temp is not None]

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(cities, temps, color="skyblue")
plt.xlabel("City")
plt.ylabel("Predicted Temperature (°F)")
plt.title("LLM Predicted Temperatures for 2024-01-06")
plt.show()

# Display results in a DataFrame
df_results = pd.DataFrame(
    list(temperatures.items()), columns=["City", "Predicted Temperature"]
)
display(df_results)

# Load the text-generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

# Define a prompt
prompt = "Once upon a time in a futuristic city,"

# Generate text
result = generator(prompt, max_length=50, num_return_sequences=1)

# Print the generated text
print("ouptut", result[0]["generated_text"])


# Enhanced temperature prediction using Gen AI with context and analysis
def predict_temperature_enhanced(city, dates_values, user_prompt):
    data_string = "\n".join(
        [f"{item['date']}: {item['value']}°F" for item in dates_values]
    )
    combined_input = f"City: {city}, Date: 2024-01-06, Data: {data_string}"
    historical_trend = "The historical temperature data for the past five days indicates an overall increasing trend."
    enhanced_prompt = (
        f"{user_prompt}\n\nHistorical Trend: {historical_trend}\n\n{combined_input}"
    )
    prompt_template = PromptTemplate(
        input_variables=["combined_input"], template="{combined_input}"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)
    prediction = chain.run(combined_input=enhanced_prompt)
    print(f"Prediction for {city}: {prediction}")
    return prediction

# Example of using Gen AI for text generation with temperature influence
def generate_weather_story(city, temperature):
  prompt = f"Write a short story about a day in {city} where the temperature is {temperature}°F."
  result = generator(prompt, max_length=100, num_return_sequences=1)
  return result[0]["generated_text"]

# Example usage with enhanced prediction and story generation:
temperatures = {}
for city, data in cities_data.items():
    prediction = predict_temperature_enhanced(city, data, user_prompt)
    temperatures[city] = extract_temperature(prediction)

for city, temp in temperatures.items():
    story = generate_weather_story(city, temp)
    print(f"\nWeather story for {city}:\n{story}")

# Load the Sentence Transformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Example sentences
sentences = [
    "This is an example sentence",
    "Each sentence is converted into an embedding",
    "Sentences are passed as a list of string.",
    "The quick brown rabbit jumps over the lazy frogs.",
]

# Compute embeddings
embeddings = model.encode(sentences)

# Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings, embeddings)

# Print the similarity matrix
cos_sim

"""# **Ask questions to LLM application about temperature**"""

#

def ask_question(question):
    # Use the rag_application_for_temperature function to get a response
    response = rag_application_for_temperature(question)
    print(f"Answer: {response}")

# Example usage:
ask_question("What is the average temperature in Paris?")
ask_question("How cold does it get in Antarctica?")

def ask_question(question):
    # Use the rag_application_for_temperature function to get a response
    response = rag_application_for_temperature(question)
    print(f"Answer: {response}")

# Example usage:
ask_question("What is the average temperature in Paris?")

# rag_application_for_temperature

def rag_application_for_temperature(user_query):
    knowledge_base = {
        "What is the average temperature in London?": "The average temperature in London is around 11°C.",
        "How hot does it get in Death Valley?": "Death Valley can reach temperatures over 50°C."
    }

    if user_query in knowledge_base:
      return knowledge_base[user_query]
    else:
      prompt = f"""Answer the following question using only factual knowledge.
      Question: {user_query}
      """
      # The output of llm(prompt) is a string, so return it directly.
      response = llm(prompt)
      return response

def ask_question(question):
    # Use the rag_application_for_temperature function to get a response
    response = rag_application_for_temperature(question)
    print(f"Answer: {response}")

# Example usage:
ask_question("What is the average temperature in Paris?")

"""## **Ask questions to RAG**"""

import os
from huggingface_hub import InferenceClient

# Set your Hugging Face API Key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize the Hugging Face LLM Client
llm_client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.1")  # Change model as needed

# Define the Knowledge Base
knowledge_base = {
    "What is the average temperature in London?": "The average temperature in London is around 11°C.",
    "How hot does it get in Death Valley?": "Death Valley can reach temperatures over 50°C.",
    "What is the coldest temperature ever recorded?": "The coldest temperature ever recorded was −128.6°F (−89.2°C) in Antarctica."
}

# Define the AI Agent Function
def rag_agent_for_temperature(user_query):
    """
    AI Agent for answering temperature-related queries.
    Uses a knowledge base and an LLM for responses.
    """

    # Step 1: Check the knowledge base first
    if user_query in knowledge_base:
        return knowledge_base[user_query]

    # Step 2: If not found, query the LLM for factual information
    prompt = f"""Answer the following question using only factual knowledge:
    Question: {user_query}
    """

    response = llm_client.chat_completion(messages=[{"role": "user", "content": prompt}])

    return response["choices"][0]["message"]["content"]

# Define an Interactive Chat Loop
def start_temperature_chat():
    """
    Interactive AI agent for temperature-related queries.
    """
    print("AI Temperature Assistant ")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("Ask a temperature-related question: ")
        if user_input.lower() == "exit":
            print("Goodbye! ")
            break

        answer = rag_agent_for_temperature(user_input)
        print(f"AI Answer: {answer}\n")

# Start the AI Agent Chat
start_temperature_chat()

"""## **Define JSON IoT sensor data in JSON format**
## **Pass as prompt the sensor data and get the output, print the results**

"""

from transformers import pipeline
import json

# Step 1: Define the IoT sensor data in JSON format
sensor_data = {
    "date": "2025-02-12",
    "temperature": "22.5°C",
    "humidity": "55%",
    "air_quality": "Good",
    "energy_usage": "15 kWh",
    "motion_detected": "No",
    "co2_level": "400 ppm",
    "sound_level": "35 dB",
    "device_activity": {
        "lights_on": 3,
        "thermostat_changes": 2,
        "door_unlocks": 1,
        "window_open": 0
    }
}

# Step 2: Convert JSON data to a formatted string for the AI model
sensor_data_str = json.dumps(sensor_data, indent=2)

# Step 3: Define the prompt for the AI model
prompt = f"""
Generate a smart home daily summary based on the following IoT sensor data:
{sensor_data_str}

The summary should be concise and user-friendly.
"""

# Step 4: Use a Hugging Face model for text generation
generator = pipeline("text-generation", model="facebook/opt-1.3b")
response = generator(prompt, max_length=200, do_sample=True)

# Step 5: Extract and display the AI-generated summary
summary = response[0]["generated_text"]
print("Smart Home Daily Summary:")
print(summary)

"""**Outout**

**Smart Home Daily Summary:**

Device set to use cuda:0
Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy. If you encode pairs of sequences (GLUE-style) with the tokenizer you can select this strategy more precisely by providing a specific strategy to `truncation`.
Smart Home Daily Summary:

Generate a smart home daily summary based on the following IoT sensor data:
{
  "date": "2025-02-12",
  "temperature": "22.5\u00b0C",
  "humidity": "55%",
  "air_quality": "Good",
  "energy_usage": "15 kWh",
  "motion_detected": "No",
  "co2_level": "400 ppm",
  "sound_level": "35 dB",
  "device_activity": {
    "lights_on": 3,
    "thermostat_changes": 2,
    "door_unlocks": 1,
    "window_open": 0
  }
}

The summary should be concise and user-friendly.

A single cloud service should be able to support this workflow with all
"""

# The End





















#















#END