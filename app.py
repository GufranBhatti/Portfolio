import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="Gufran Bhatti", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2024 Gufran Bhatti';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Assets for about me
img_utown = Image.open("images/aboutme.jpeg")
img_lh = Image.open("images/uni-cor.jpg")
img_con = Image.open("images/contact.jpg")

# Assets for education
img_tpjc = Image.open("images/school.jpg")
img_nus = Image.open("images/kiet.jpg")
img_poc = Image.open("images/college.jpg")

# Assets for experiences
img_groundup = Image.open("images/spark.png")
img_hedgedrip = Image.open("images/precisionbird.png")

#images for projects
img_fyp = Image.open("images/research.png")
img_lfb = Image.open("images/lfb.jpg")
img_hou = Image.open("images/housepred.jpg")
img_zomato = Image.open('images/zomato.jpg')
img_heart = Image.open("images/heart.jpeg")
img_reckless = Image.open("images/reckless.jpeg")

#images for certifications
img_uda = Image.open("images/udacity.jpg")
img_cou = Image.open("images/coursera.png")
img_fcc = Image.open("images/fcc.png")

# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Gufran Bhatti",
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Publications", "Certifications", "Resume", "Contact"],
                         icons=['person fill', 'clock history', 'tools', 'book half', 'clipboard', 'globe', 'star fill', 'paperclip', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "menu-icon": {"color": "darkorange", "font-size": "20px"},
        "menu-title": {"color": "black"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "color": "#000000", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    linkedin_url = "https://www.linkedin.com/in/gufran-bhatti-80568822a/"
    github_url = "https://github.com/GufranBhatti"
    email_url = "mailto:gufranbhatti5@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Gufran Bhatti")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Python Developer/Aspiring Data Analyst")
            st.write("👋🏻 Hi, I'm Gufran! I'm a computer science graduate based in Pakistan. With previous hands-on involvement in data science and Python development roles, I am actively exploring distinctive opportunities to further enhance my skill set. Eager to broaden my expertise, I am currently in search of unique job experiences that align with my passion and ambitions, as I continue to progress in my career journey.")
            st.write("💼 With the post-COVID era unfolding, I see the potential for applying data science across diverse industries. In response to the rising demand for data analytics in various sectors, I am eager to explore opportunities for my initial full-time position, aiming to contribute my skills and insights to different industry landscapes.")
            st.write("🏋🏻 In addition, I like to exercise in the gym, run, write, play football and video games and... enjoy eating good food in my free time!")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Data Analysis, Automation, Predictive AI models")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst")
            st.write("📄 [Resume](https://drive.google.com/file/d/1Dc0PICIDzLQUs6xIvrPhwsFx9BYixncp/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)

# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_hedgedrip)
        with text_column:
            st.subheader("Python Developer, [PrecisionBird](https://www.linkedin.com/company/precision-bird/about/)")
            st.write("*September 2023 to Present*")
            st.markdown("""
            - Automate tasks like downloading and processing spatial data using python to speed up the productivity.
            - Write python scripts to solve problems related to spatial data analytics.
            - Use prebuilt object detection models and tune them to detect plants in crop images.
            - Learnt Django framework and built a basic website using postgresql as database.
            - Use GIS tools to like ArcGIS Pro, Google Earth Pro, etc. to analyze and process sentinel-2 data.
            
            `Automation` `Object Detection` `Spatial Data Analysis` `Django`
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_groundup)
        with text_column:
            st.subheader("Data Science Intern, [The Sparks Foundation](https://www.thesparksfoundationsingapore.org/)")
            st.write("*October to November 2022*")
            st.markdown("""
            - Primary task was to perform exploratory data analysis on various datasets.
            - Used basic machine learning models on supervised datasets.
            
            `Python` `Visualization` `Data Analytics` `EDA` `Machine Learning` `Team Work` `Scikit-Learn` `Matplotlib`
            """)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`Python`, `SQL`, `Java`, `C#`")
    txt3("Academic Interests","`Data Visualization`, `Data Analysis`, `Automation`, `Predictive AI models`")
    txt3("Data Visualization", "`matplotlib`, `seaborn`, `Plotly`, `GIS`, `Tableau`, `Power BI`")
    txt3("Database Systems", "`MySQL`, `PostgreSQL`")
    txt3("Cloud Platforms", "`Streamlit Cloud`")
    txt3("Design and Front-end Development", "`Canva`, `Streamlit`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`")
    txt3("Task Management Tools", "`Slack`")
    txt3("Miscellaneous", "`Microsoft Office`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    st.subheader("Summary")
    st.write("*Summary of education from school till university*")
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_nus)
        with text_column:
            st.subheader("Bachelor of Science - [Computer Science](https://cocis.kiet.edu.pk/bs-computer-science/), [Karachi Institute of Economics and Technology](https://kiet.edu.pk/) (2019-2023)")
            st.write("Relevant Coursework: Programming Fundamentals, OOP, Discrete Maths, Data Structures and Algorithms, Database Management System, Linear Algebra, Multivariable Calculus, Artificial Intelligence, Probability and Statistics, Operating System, Cryptography, Automata, Compiler Construction")
            st.markdown("""
            - Scholarship in Fall 2019.
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_poc)
        with text_column:
            st.subheader("Intermediate - Pre-Engineering, Government Degree College Gulshan-e-Iqbal Block 7 (2016-2018)")
            st.write("Coursework: Chemistry, Physics, Mathematics, Urdu, English, Islamiat, Pakistan Studies")
            st.markdown("""
            - Football (Futsal 5v5, 6v6, 7v7)
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_tpjc)
        with text_column:
            st.subheader("Matriculation in Science - Al-Badr School (2014 - 2016)")
            st.write("Coursework: Chemistry, Physics, Mathematics, Urdu, English, Islamiat, Pakistan Studies")
            st.markdown(""" 
            - Basketball
            - Tug of War
            """)

elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Intrusion Detection Using Machine Learning and Deep Learning for IoT (FYP)")
            st.write("*Final Year Project of my BSCS degree*")
            st.markdown("""
            - Implemented Decision Trees (DT), Random Forest (RF), and Bi-LSTM on ARP_MITM and SSDP FLOOD datasets.
            - Utilized concatenated datasets with varying training/testing ratios for DT and RF, achieving accuracy over 99%, with Random Forest outperforming other models.
            - Developed a prototype with a user-friendly front-end for dataset upload, where the back-end model accurately categorizes packets as normal or malicious, presenting performance metrics and a confusion matrix for model evaluation.
            - The research work, encompassing the implementation of DT, RF, and Bi-LSTM on ARP_MITM and SSDP FLOOD datasets, was thoroughly documented and resulted in the publication of a research paper on IEEE Xplore.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/GufranBhatti/Intrusion-Detection-Using-Machine-Learning-And-Deep-Learning-FYP-",)
        with image_column:
            st.image(img_fyp)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Mining on LFB Dataset")
            st.write("*Self-initiated project*")
            st.markdown("""
            - Analyzed the LFB dataset, encompassing details on call date/time, incident category, location, and response information.
            - Successfully identified and addressed business problems, proposing effective solutions.
            - Conducted thorough data preprocessing, constructed models, and interpreted/evaluated them.
            - Utilized Jupyter Notebook for the entire project, ensuring clear documentation and meeting specified requirements in each observation.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/GufranBhatti/Data-Mining-Project-For-LFB-Dataset",)
        with image_column:
            st.image(img_lfb)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Advanced Regression Technique for House Prices")
            st.write("*Competition on kaggle*")
            st.markdown("""
            - Utilized a dataset containing house descriptions as features and house prices as the target feature.
            - Conducted data preprocessing, which included handling null values, applying various encoding techniques, and selecting optimal features.
            - Implemented different regression algorithms and neural networks to train the model.
            - The project focused on predicting house prices based on the given dataset and involved both traditional regression algorithms and advanced neural network approaches.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/GufranBhatti/house-prices-advanced-regression-techniques",)
        with image_column:
            st.image(img_hou)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("EDA on Zomato Dataset")
            st.write("*Self-initiated project")
            st.markdown("""
            - Explored relationships between features and performed basic data analysis operations.
            - Showcased all the relationships, patterns, and features using Matplotlib for a comprehensive understanding.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/GufranBhatti/EDA-SampleSuperStore",)
        with image_column:
            st.image(img_zomato)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Reckless Driving Detection")
            st.write("*Ubiquitous Computing and IoT Course project*")
            st.markdown("""
            - Utilized a Kaggle dataset to train an AI model for detecting reckless driving.
            - Project repository includes explanatory Word documents detailing the project and Jupyter notebook files for model training.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/GufranBhatti/Reckless-Driving-Detection",)
        with image_column:
            st.image(img_reckless)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Heart Disease Prediction using Logistic Regression")
            st.write("*Self-initiated project as a beginner*")
            st.markdown("""
            - Worked on a heart disease dataset downloaded from Kaggle.
            - Utilized logistic regression to train a model.
            - Achieved an accuracy of 80% on the test data.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/GufranBhatti/Heart-disease-prediction-using-logistic-regression",)
        with image_column:
            st.image(img_heart)
    
elif choose == "Publications":
    # Create section for Competitions
    #st.write("---")
    st.header("Publications")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_fyp)
            #st.empty()
        with text_column:
            st.subheader("[Efficient & Sustainable Intrusion Detection System Using Machine Learning & Deep Learning for IoT](https://ieeexplore.ieee.org/document/10099152) - Hosted by [Sukkur IBA University](https://www.iba-suk.edu.pk/)")
            st.write("Everything is evolving toward IoT (Internet of Things) and online-based in our technological environment. The number of IoT devices and ubiquitous computing systems are growing exponentially. This also increases the risk of network breach. To cater this issue many researchers proposed different techniques and get great results but it can be better since everything in online and it's a matter of security and privacy. This paper presents an efficient and sustainable intrusion detection system by the concatenation of two well-known state of the art “kitsune” datasets (ARP MITM and SSDP Flood). Random Forest, decision tree, and Bi-LSTM (Bi-Directional Long Short Term Memory) were implemented in different training and testing ratios and different numbers of layers. Performance measures show that all the models achieved over 99% accuracy but random forest outperforms both models on the concatenated dataset. Both attacks are determined by the given model hence increasing the performance and the system will notify in case of any malicious activity.")
            mention(label="Research Paper", icon="📄", url="https://ieeexplore.ieee.org/document/10099152",)

elif choose == "Certifications":
    # Create section for Competitions
    #st.write("---")
    st.header("Certifications")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_cou)
            #st.empty()
        with text_column:
            st.subheader("[Data Analysis and Visualization with Power BI](https://www.coursera.org/learn/data-analysis-and-visualization-with-power-bi) - Hosted by [Coursera](https://www.coursera.org/)")
            st.write("Data Analysis and Visualization with Power BI program offers a comprehensive understanding of key skills essential for effective data analysis and visualization in Power BI. They will learn how to add various visualizations to reports and dashboards, enhancing the presentation of data insights. Additionally, learners will master the art of designing accessible reports and dashboards, ensuring inclusivity and usability for all users.")
            mention(label="Verification", icon="📄", url="https://www.coursera.org/account/accomplishments/verify/94CPNJJWSEWE",)
    
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_cou)
            #st.empty()
        with text_column:
            st.subheader("[Data Modeling in Power BI](https://www.coursera.org/learn/data-modeling-in-power-bi) - Hosted by [Coursera](https://www.coursera.org/)")
            st.write("Data Modeling in Power BI program offers a comprehensive understanding of data modeling, DAX expressions, and performance optimization in Power BI. Throughout the course, learners will learn how to create and maintain relationships in a data model, including forming models using multiple schemas like the Star Schema. Additionally, learners will master the basics of DAX and how to write calculations to create elements and conduct analysis in Power BI. They will be able to create calculated columns and measures, perform time intelligence calculations, and optimize performance using tools such as the performance analyzer and DirectQuery features.")
            mention(label="Verification", icon="📄", url="https://www.coursera.org/account/accomplishments/certificate/9YTRBXV7BBQF",)
            
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_cou)
            #st.empty()
        with text_column:
            st.subheader("[Extract, Transform and Load Data in Power BI](https://www.coursera.org/learn/extract-transform-and-load-data-in-power-bi) - Hosted by [Coursera](https://www.coursera.org/)")
            st.write("Extract, Transform and Load Data in Power BI program offers valuable skills in setting up data sources and configuring storage modes to effectively manage data within Power BI. Throughout the course, learners will delve into the cleaning and transformation of data for improved accuracy and usability in analysis. Also learners will utilize profiling tools, becoming adept at identifying data anomalies, ensuring data quality at every step. Moreover, learners will hone their ability to reference queries and dataflows, harnessing the power of the Advanced Editor to customize data transformations to meet specific business needs.")
            mention(label="Verification", icon="📄", url="https://www.coursera.org/account/accomplishments/verify/733M5WBFBYZ3",)
            
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_uda)
            #st.empty()
        with text_column:
            st.subheader("[AI Programming with Python](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089?coupon=BLACKFRIDAY50&utm_source=gsem_brand&utm_source=gsem_brand&utm_medium=ads_r&utm_medium=ads_r&utm_campaign=19167921312_c_individuals&utm_campaign=19167921312_c_individuals&utm_term=143524477399&utm_term=143524477399&utm_keyword=udacity%20python%20ai_e&utm_keyword=udacity%20python%20ai_e&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh31uyaTDstehCFlRgtrxSI-M2ektMJj8FidIloao9lzSKN66LbiP54aAq9MEALw_wcB) - Hosted by [Udacity](https://www.udacity.com/)")
            st.write("AI Programming with Python Nanodegree program offers a beginner-friendly exploration into Python AI programming. This course covers Python, NumPy, Pandas, Matplotlib, PyTorch, and Linear Algebra, laying a solid foundation for building neural networks. You'll engage in practical projects like vector visualization and Python data types, gaining real-world experience. Taught by experts like Mat Leonard and Luis Serrano, this Python AI course combines hands-on learning with industry insights, making it ideal for those starting in AI.")
            mention(label="Verification", icon="📄", url="https://graduation.udacity.com/confirm/e/cc349c3a-0ae7-11ee-8a9c-9752588c03be",)

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_cou)
            #st.empty()
        with text_column:
            st.subheader("[Neural Networks and Deep Learning](https://www.coursera.org/learn/neural-networks-deep-learning) - Hosted by [Coursera](https://www.coursera.org/)")
            st.write("Neural Networks and Deep Learning program offers comprehensive knowledge and skills in the field of artificial intelligence, specifically focusing on artificial neural networks and deep learning. Throughout the course, learners will delve into the foundational concepts of neural networks, exploring topics such as backpropagation, Python programming, and neural network architecture.")
            mention(label="Verification", icon="📄", url="https://www.coursera.org/account/accomplishments/certificate/4JLE5Y3S7JKV",)

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_cou)
            #st.empty()
        with text_column:
            st.subheader("[Databases and SQL for Data Science with Python](https://www.coursera.org/learn/sql-data-science?specialization=bi-foundations-sql-etl-data-warehouse&utm_source=gg&utm_medium=sem&utm_campaign=B2C_APAC__branded_FTCOF_courseraplus_arte_PMax_set3&utm_content=Degree&campaignid=20520161513&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&adpostion=&creativeid=&hide_mobile_promo&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh2GFJhFEQtR6Xd8e8foJyJMkz0V0YtQ7gZsl1XlGWLUY5iwpOMk90oaAsMDEALw_wcB) - Hosted by [Coursera](https://www.coursera.org/)")
            st.write("Databases and SQL for Data Science with Python program offers essential skills in analyzing data within a database using both SQL and Python. The curriculum covers the creation of a relational database and the management of multiple tables through Data Definition Language (DDL) commands. Learners will progress from constructing basic to intermediate level SQL queries using Data Manipulation Language (DML) commands, gradually advancing to more powerful queries through the application of advanced SQL techniques. These techniques include working with views, transactions, stored procedures, and joins. The skills gained encompass proficiency in Python programming, understanding cloud databases, expertise in Relational Database Management System (RDBMS), and proficiency in SQL.")
            mention(label="Verification", icon="📄", url="https://www.coursera.org/account/accomplishments/certificate/PTWDHW22D5D5",)

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_fcc)
            #st.empty()
        with text_column:
            st.subheader("[Machine Learning with Python](https://www.freecodecamp.org/learn/machine-learning-with-python/) - Hosted by [FreeCodeCamp](https://www.freecodecamp.org/learn)")
            st.write("Machine Learning with Python program offers a beginner-friendly exploration into Python ML programming. In this course, you'll use the TensorFlow framework to build several neural networks and explore more advanced techniques like natural language processing and reinforcement learning. You'll also dive into neural networks, and learn the principles behind how deep, recurrent, and convolutional neural networks work.")
            mention(label="Verification", icon="📄", url="https://www.freecodecamp.org/certification/GufranBhatti/machine-learning-with-python-v7",)

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_fcc)
            #st.empty()
        with text_column:
            st.subheader("[Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) - Hosted by [FreeCodeCamp](https://www.freecodecamp.org/learn)")
            st.write("Data Analysis with Python program offers a beginner-friendly exploration into Python programming for data analytics. In this course, you'll learn the fundamentals of data analysis with Python. By the end of this certification, you'll know how to read data from sources like CSVs and SQL, and how to use libraries like Numpy, Pandas, Matplotlib, and Seaborn to process and visualize data.")
            mention(label="Verification", icon="📄", url="https://www.freecodecamp.org/certification/GufranBhatti/data-analysis-with-python-v7",)


elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1Dc0PICIDzLQUs6xIvrPhwsFx9BYixncp/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume**"), unsafe_allow_html=True)
    show_pdf("Gufran_Resume_CS.pdf")
    # with open("Gufran_Resume_CS.pdf", "rb") as file:
    #     btn = st.download_button(
    #         label="Download Resume",
    #         data=file,
    #         file_name="Gufran_Resume_CS.pdf",
    #         mime="application/pdf"
    #     )


elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may reach out to me at gufranbhatti5@gmail.com")
            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/gufran-bhatti-80568822a/"
            github_url = "https://github.com/GufranBhatti"
            email_url = "mailto:gufranbhatti5@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        with image_column:
            st.image(img_con)
st.markdown("*Copyright © 2024 Gufran Bhatti*")

