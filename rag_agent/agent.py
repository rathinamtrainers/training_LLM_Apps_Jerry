from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

ask_vertex_retrieval = VertexAiRagRetrieval(
    name="retrieve_rag_documentation",
    description=(
        'Use this tool to retrieve documentation and reference materials for the question from the RAG corpus.'
    ),
    rag_resources=[
        rag.RagResource(rag_corpus="projects/students-demo-ai-2025/locations/us-central1/ragCorpora/4611686018427387904")
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="rag_agent",
    instruction="""
    You are an AI assistant with access to specialized corpus of documents.
    Your role is to provide accurate and concise answers to questions based
    on documents that are retrievable using ask_vertex_retrieval tool. If 
    you believe that the user is just chatting and having a casual conversation,
    don't use the retrieval tool.
    
    But if the user is asking a specific question about a knowledge they expect
    you to have, you can use the retrieval tool to fetch the most relevant information. 
    """,
    tools=[ask_vertex_retrieval]
)