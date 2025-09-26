from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

# List collections
print("Collections:", client.get_collections())

# Get stored points from CrewAI collection
points = client.scroll(
    collection_name="CrewAI",
    limit=5,
)
print("Stored memory points:", points)
