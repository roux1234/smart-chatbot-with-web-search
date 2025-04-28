from langchain_community.llms.fake import FakeListLLM
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from duckduckgo_search import DDGS
import random

# Set up fake LLM for fun/random responses
responses = [
    "That's a great question! Let me think...",
    "I'm not sure, but here's what I think!",
    "Interesting! I'll try to answer as best as I can.",
    "Here's something you might find helpful!",
    "Let's figure it out together!"
]
llm = FakeListLLM(responses=random.sample(responses, len(responses)))

# Create memory
memory = ConversationBufferMemory()

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

# Function to search web using DuckDuckGo
def search_web(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=2)
        combined_results = "\n".join([result['body'] for result in results])
    return combined_results if combined_results else "Sorry, I couldn't find anything online."

# Main loop
print("\n💬 Welcome to your Smart Chatbot! Type 'exit' to quit.")
while True:
    query = input("\nYou: ")
    if query.lower() == "exit":
        break

    # Decide whether to search the web
    keywords = ["who", "what", "when", "where", "how", "define", "information", "tell me about", "news", "latest"]
    if any(keyword in query.lower() for keyword in keywords):
        print("\n🔎 Fetching information from the web...")
        web_answer = search_web(query)
        print(f"\nBot (Web Search): {web_answer}")
    else:
        # Otherwise, use the conversation LLM
        response = conversation.predict(input=query)
        print(f"\nBot (Memory Chat): {response}")
