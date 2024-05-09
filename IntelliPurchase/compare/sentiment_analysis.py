from blog.models import Sentiment
import plotly.express as px

def plot_sentiment(product_id):
    sentiment = Sentiment.objects.filter(product_id=product_id)
    data = {
        'Sentiment': ['Pin', 'General', 'Service', 'Others'],
        'Score': [sentiment.s_pin, sentiment.s_general, sentiment.s_service, sentiment.s_others]
    }
    print(data)

