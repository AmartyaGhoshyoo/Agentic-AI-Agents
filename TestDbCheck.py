#!/usr/bin/env python3
"""
Simple Database Explorer for Agno Agent
This script explores the SQLite database and explains LanceDB structure
"""

import sqlite3
import os
import json

def explore_sqlite_db():
    """Explore the SQLite agent.db file"""
    print("=" * 60)
    print("EXPLORING SQLITE DATABASE (agent.db)")
    print("=" * 60)
    
    # Use absolute path
    db_path = "/Users/amartyaghosh/Library/Mobile Documents/com~apple~TextEdit/Documents/Projects ML/Heart Disease Prediction/Agentic AI/Agentic -AI- Agents/CrewAI/crewai_storage/long_term_memory_storage.db"
    
    if not os.path.exists(db_path):
        print(f"Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"Tables found: {[table[0] for table in tables]}")
        print()
        
        for table in tables:
            table_name = table[0]
            print(f"Table: {table_name}")
            print("-" * 40)
            
            # Get table schema
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            print("Columns:")
            for col in columns:
                print(f"  {col[1]} ({col[2]})")
            print()
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"Row count: {count}")
            
            # Show sample data (first 5 rows)
            if count > 0:
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                print("Sample data:")
                for i, row in enumerate(rows):
                    print(f"  Row {i+1}: {row}")
            print()
            
        conn.close()
        
    except Exception as e:
        print(f"Error exploring SQLite database: {e}")

def explain_lancedb_structure():
    """Explain what each LanceDB directory contains"""
    print("=" * 60)
    print("LANCEDB STRUCTURE EXPLANATION")
    print("=" * 60)
    
    lancedb_path = "/Users/amartyaghosh/Library/Mobile Documents/com~apple~TextEdit/Documents/Projects ML/Heart Disease Prediction/Agentic AI/Agentic -AI- Agents/Agno/AgAgents Leaning Notes/tmp/lancedb/agno_docs.lance"
    
    print("LanceDB Directory Structure:")
    print()
    
    # Explain each directory
    directories = {
        "_indices": {
            "purpose": "Contains search indices for fast vector similarity search",
            "files": "Fast search index files (.fast, .idx, .store, .term, .pos)",
            "explanation": "These files enable the agent to quickly find relevant text chunks when searching the knowledge base"
        },
        "_versions": {
            "purpose": "Contains version manifests for tracking changes and rollbacks",
            "files": "Version manifest files (.manifest)",
            "explanation": "Each .manifest file represents a snapshot of the database at a specific point in time, enabling version control and rollbacks"
        },
        "_transactions": {
            "purpose": "Contains transaction logs for ACID compliance and data integrity",
            "files": "Transaction files (.txn)",
            "explanation": "These files log all database operations to ensure data consistency and allow recovery from failures"
        },
        "data": {
            "purpose": "Contains the actual data chunks in Lance format",
            "files": "Data files (.lance)",
            "explanation": "Each .lance file contains the actual text chunks and their vector embeddings from the Agno documentation"
        }
    }
    
    for dir_name, info in directories.items():
        dir_path = os.path.join(lancedb_path, dir_name)
        if os.path.exists(dir_path):
            file_count = len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])
            print(f"{dir_name}/:")
            print(f"  Purpose: {info['purpose']}")
            print(f"  Files: {file_count} files")
            print(f"  File types: {info['files']}")
            print(f"  Explanation: {info['explanation']}")
            
            # Show some sample files
            if file_count > 0:
                sample_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))][:3]
                print(f"  Sample files: {sample_files}")
            print()
        else:
            print(f"{dir_name}/: Directory not found")
            print()

def show_file_counts():
    """Show the count of files in each LanceDB directory"""
    print("=" * 60)
    print("LANCEDB FILE COUNTS")
    print("=" * 60)
    
    lancedb_path = "/Users/amartyaghosh/Library/Mobile Documents/com~apple~TextEdit/Documents/Projects ML/Heart Disease Prediction/Agentic AI/Agentic -AI- Agents/Agno/AgAgents Leaning Notes/tmp/lancedb/agno_docs.lance"
    
    for dir_name in ["_indices", "_versions", "_transactions", "data"]:
        dir_path = os.path.join(lancedb_path, dir_name)
        if os.path.exists(dir_path):
            files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
            print(f"{dir_name}/: {len(files)} files")
            
            # Group files by extension
            extensions = {}
            for file in files:
                ext = os.path.splitext(file)[1]
                extensions[ext] = extensions.get(ext, 0) + 1
            
            for ext, count in extensions.items():
                print(f"  {ext}: {count} files")
        else:
            print(f"{dir_name}/: Directory not found")
        print()

if __name__ == "__main__":
    print("Crewai DATABASE EXPLORER")
    print("=" * 60)
    
    # Explore SQLite database
    explore_sqlite_db()
    
    # Explain LanceDB structure
    # explain_lancedb_structure()
    
    # Show file counts
    # show_file_counts()
    
    print("=" * 60)
    print("EXPLORATION COMPLETE")
    print("=" * 60)



"""
Crewai DATABASE EXPLORER
============================================================
============================================================
EXPLORING SQLITE DATABASE (agent.db)
============================================================
Tables found: ['long_term_memories', 'sqlite_sequence']

Table: long_term_memories
----------------------------------------
Columns:
  id (INTEGER)
  task_description (TEXT)
  metadata (TEXT)
  datetime (TEXT)
  score (REAL)

Row count: 10
Sample data:
  Row 1: (1, 'Find places to live, eat, and visit in san franscio.', '{"suggestions": ["Include a brief introduction or summary about San Francisco at the beginning for better context.", "Add a map or links to maps to better visualize the neighborhoods and attractions.", "Provide a section for public transportation options and accessibility for each neighborhood and attraction.", "Include price ranges or budget considerations for dining options more explicitly.", "Add user reviews or ratings sources to enhance credibility of recommendations.", "Ensure consistent formatting for URLs and consider hyperlinking them in the text for easier access.", "Add a few key events or cultural highlights to enrich the visiting experience section."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in san franscio. **IMPORTANT Don\'t search again if you already have the information on "}', '1758867421.069178', 9.0)
  Row 2: (2, 'Find places to live, eat, and visit in san franscio.', '{"suggestions": ["Correct the spelling of \'San Francisco\' in the task description and output for accuracy.", "Include specific criteria or characteristics for each place to live, eat, and visit to enhance clarity.", "Add more diverse food options including more ethnic and budget-friendly choices to cater to a wider audience.", "Provide contact information or public transit options for places which would be helpful for visitors.", "Incorporate brief historical or cultural context for the places to visit to enrich the information provided."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in san franscio. **IMPORTANT Don\'t search again if you already have the information on "}', '1758867883.42885', 9.0)
  Row 3: (3, 'Find places to live, eat, and visit in Bangladesh.', '{"suggestions": ["Include more detailed information about the cost of living in each residential area for better decision making.", "Add more dining options in smaller cities or towns to provide a broader perspective on eating places in Bangladesh.", "Incorporate transportation and accessibility information for the places to live, eat, and visit.", "Provide seasonal recommendations or best times to visit each tourist spot for more practical planning.", "Include user reviews or ratings where possible to give an idea of popularity or satisfaction."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in Bangladesh. **IMPORTANT Don\'t search again if you already have the information on "}', '1758868367.942014', 9.0)
  Row 4: (4, 'Find places to live, eat, and visit in Bangladesh.', '{"suggestions": ["Include more budget-friendly living options for diverse economic groups.", "Add links or resources for further information or bookings.", "Incorporate more cultural or event-based attractions for visitors.", "Provide food hygiene tips or recommendations for safe eating experiences.", "Consider adding seasonal variations for travel and living conditions."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in Bangladesh. **IMPORTANT Don\'t search again if you already have the information on "}', '1758869145.718981', 9.0)
  Row 5: (5, 'Find places to live, eat, and visit in india.', '{"suggestions": ["Include more specific neighborhoods or localities for each city to enhance planning accuracy.", "Add tips for seasonal considerations affecting living conditions and tourism, such as climate variations.", "Incorporate budget ranges for dining options alongside best restaurants for a wider audience appeal.", "Provide transportation information related to each city or tourist place to aid logistics.", "Include a section for cultural norms or travel tips to make the guide more comprehensive."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in india. **IMPORTANT Don\'t search again if you already have the information on "}', '1758869224.9159548', 9.0)
  Row 6: (6, 'Find places to live, eat, and visit in san fransisco.', '{"suggestions": ["Include transportation options and accessibility details for each recommended neighborhood and attraction.", "Add a section for budget-friendly or less expensive options to cater to a wider audience with varied financial capabilities.", "Provide links to official or authoritative sources for all mentioned places for better credibility.", "Incorporate user reviews or ratings to give a sense of popularity and visitor satisfaction.", "Consider adding a seasonal or event-based guide to highlight when to visit certain places for the best experience."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in san fransisco. **IMPORTANT Don\'t search again if you already have the information on "}', '1758882860.8653262', 9.0)
  Row 7: (7, 'Find places to live, eat, and visit in india.', '{"suggestions": ["Include more diverse cities and regions of India to cover eastern and northeastern parts of the country for comprehensive representation.", "Add more specific dining recommendations including type of cuisine and famous dishes for each city.", "Provide estimated costs or budget ranges for living accommodation.", "Add seasonal travel tips for each city/place to help travelers plan better.", "Consider including public holidays or festival timings which might affect travel plans or availability.", "Use standardized formatting for neighborhood and restaurant names for clarity."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in india. **IMPORTANT Don\'t search again if you already have the information on "}', '1758883033.947211', 9.0)
  Row 8: (8, 'Find places to live, eat, and visit in srilanka.', '{"suggestions": ["Include more visual aids such as maps or images in the output for better user engagement.", "Add estimated cost ranges for living, dining, and visiting places to provide financial context.", "Provide contact details or website links for recommended places to facilitate easy access to more information.", "Segment the dining options by cuisine type or budget to better cater to diverse preferences.", "Include current travel tips or restrictions relevant to Sri Lanka to enhance the practicality of the travel guide."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in srilanka. **IMPORTANT Don\'t search again if you already have the information on "}', '1758883097.4718568', 9.0)
  Row 9: (9, 'Find places to live, eat, and visit in malaysia.', '{"suggestions": ["Include brief information about the cultural diversity and languages spoken to enhance the context for living and visiting Malaysia.", "Add recommended accommodation options or neighborhoods with price ranges for better guidance on living expenses.", "Incorporate popular local events or festivals to enrich the visiting experience.", "Provide a summary of transportation options at the end of each major section for convenience.", "Include a few top recommended restaurants or street food vendors per city for more practical eating options."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in malaysia. **IMPORTANT Don\'t search again if you already have the information on "}', '1758883269.506569', 9.0)
  Row 10: (10, 'Find places to live, eat, and visit in dubai.', '{"suggestions": ["Include specific criteria for the places listed such as price range or target demographic to improve relevance.", "Add user reviews or ratings to enhance trustworthiness of recommendations.", "Integrate a map or location details for easier geographic context.", "Offer seasonal or event-based recommendations for eating and visiting.", "Provide some lesser-known local gems along with popular spots for a balanced guide."], "quality": 9.0, "agent": "Personalized Travel Planner Agent", "expected_output": "A detailed list of places to live, eat, and visit in dubai. **IMPORTANT Don\'t search again if you already have the information on "}', '1758883369.994993', 9.0)

Table: sqlite_sequence
----------------------------------------
Columns:
  name ()
  seq ()

Row count: 1
Sample data:
  Row 1: ('long_term_memories', 10)

============================================================
EXPLORATION COMPLETE
============================================================



"""