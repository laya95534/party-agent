from smolagents import Tool
from langchain_community.retrievers import BM25Retriever
import datasets
from langchain_core.documents import Document

# Load dataset
guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")

# Convert dataset into documents
docs = [
    Document(
        page_content=f"""
Name: {guest['name']}
Relation: {guest['relation']}
Description: {guest['description']}
Email: {guest['email']}
""",
        metadata={"name": guest["name"]}
    )
    for guest in guest_dataset
]

# Create tool
class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = "Get guest information using name or relation"
    inputs = {
        "query": {
            "type": "string",
            "description": "Guest name"
        }
    }
    output_type = "string"

    def __init__(self):
        self.is_initialized = True
        self.retriever = BM25Retriever.from_documents(docs)

    def forward(self, query: str):
        results = self.retriever.invoke(query)
        if results:
            return "\n\n".join([doc.page_content for doc in results[:2]])
        return "No guest found"

# Initialize tool
guest_tool = GuestInfoRetrieverTool()