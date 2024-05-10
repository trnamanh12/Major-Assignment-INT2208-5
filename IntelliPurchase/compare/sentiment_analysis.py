from blog.models import Sentiment
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def plot_sentiment(product_id, company_id):
    aspects = ['Pin', 'Tổng quan', 'Dịch vụ CSKH', 'Những khía cạnh khác']
    sentiments = ['Positive', 'Neutral', 'Negative']

    sentiment = Sentiment.objects.filter(product_id=product_id, company_id=company_id)[0]

    sentiments_ratio = [                                     
        eval(sentiment.s_pin.replace(' 0', ',0')),
        eval(sentiment.s_general.replace(' 0', ',0')),
        eval(sentiment.s_service.replace(' 0', ',0')),
        eval(sentiment.s_others.replace(' 0', ',0'))
    ]
    
        # Tạo subplot với loại 'pie' và khoảng trống
    fig = make_subplots(rows=2, cols=2, subplot_titles=aspects, specs=[[{'type':'pie'}, {'type':'pie'}],[{'type':'pie'}, {'type':'pie'}]], horizontal_spacing=0.05, vertical_spacing=0.2)

    # Vẽ biểu đồ pie cho mỗi khía cạnh
    for i, aspect in enumerate(aspects):
        row = 1 if i < 2 else 2
        col = i % 2 + 1
        labels = sentiments
        values = [sentiments_ratio[i][2], sentiments_ratio[i][1], sentiments_ratio[i][0]] 
        
        # Tạo biểu đồ pie và thêm vào subplot tương ứng
        fig.add_trace(go.Pie(labels=labels, values=values, name=aspect), row=row, col=col)


    # Cài đặt layout
    fig.update_layout(
        title=f'<b>Cảm xúc trung bình của <span style="color:#FF5733">{sentiment.product.product_name}</span> trên <span style="color:#ff8a3c">{sentiment.company_id.company_name}</span></b>',
        width=600,
        height=350,
        title_x=0.5
    )
    return fig

