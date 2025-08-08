import json
import os
from datetime import datetime

def read_json_data(filename="agfunder_articles.json"):
    """Read the articles from JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            articles = json.load(f)
        print(f"Successfully read {len(articles)} articles from {filename}")
        return articles
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

def generate_html(articles):
    """Generate HTML content from articles data"""
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgFunder News Articles</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            font-weight: 300;
        }}
        
        .header p {{
            opacity: 0.9;
            font-size: 1.1rem;
        }}
        
        .stats {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            border-bottom: 1px solid #e9ecef;
            font-weight: 600;
            color: #2c3e50;
        }}
        
        .articles {{
            padding: 30px;
        }}
        
        .article {{
            background: #f8f9fa;
            margin-bottom: 20px;
            border-radius: 10px;
            overflow: hidden;
            border-left: 5px solid #667eea;
            transition: all 0.3s ease;
        }}
        
        .article:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        
        .article-content {{
            padding: 25px;
        }}
        
        .article-title {{
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 15px;
            line-height: 1.4;
        }}
        
        .article-title a {{
            color: #2c3e50;
            text-decoration: none;
            transition: color 0.3s ease;
        }}
        
        .article-title a:hover {{
            color: #667eea;
        }}
        
        .article-url {{
            color: #6c757d;
            font-size: 0.9rem;
            word-break: break-all;
            background: white;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #e9ecef;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 0.9rem;
            opacity: 0.8;
        }}
        
        .no-articles {{
            text-align: center;
            padding: 60px 20px;
            color: #6c757d;
            font-size: 1.2rem;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2rem;
            }}
            
            .articles {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 AgFunder News Articles</h1>
            <p>Latest articles scraped from AgFunder News</p>
        </div>
        
        <div class="stats">
            Found {len(articles)} articles • Generated on {current_time}
        </div>
        
        <div class="articles">'''
    
    if not articles:
        html_content += '''
            <div class="no-articles">
                No articles found. Please check your JSON file.
            </div>'''
    else:
        for i, article in enumerate(articles, 1):
            title = article.get('title', 'Untitled Article')
            url = article.get('url', '#')
            
            html_content += f'''
            <div class="article">
                <div class="article-content">
                    <div class="article-title">
                        <a href="{url}" target="_blank" title="Open article in new tab">
                            {i}. {title}
                        </a>
                    </div>
                    <div class="article-url">
                        🔗 {url}
                    </div>
                </div>
            </div>'''
    
    html_content += '''
        </div>
        
        <div class="footer">
            Generated by AgFunder News Scraper
        </div>
    </div>
</body>
</html>'''
    
    return html_content

def create_html_file(html_content, filename="index.html"):
    """Write HTML content to file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Successfully created {filename}")
        return True
    except Exception as e:
        print(f"Error creating {filename}: {e}")
        return False

def main():
    """Main function to convert JSON to HTML"""
    print("Converting JSON to HTML...")
    
    # Read the JSON data
    articles = read_json_data()
    
    if not articles:
        print("No articles to process.")
        return
    
    # Generate HTML content
    html_content = generate_html(articles)
    
    # Create the HTML file
    success = create_html_file(html_content)
    
    if success:
        print(f"✅ Successfully converted {len(articles)} articles to index.html")
        print("You can now open index.html in your web browser!")
    else:
        print("❌ Failed to create HTML file")

if __name__ == "__main__":
    main()