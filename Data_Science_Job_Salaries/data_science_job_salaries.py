# Data
import pandas as pd
import numpy as np

# Visualization
import plotly as plotly
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
colors = ['#494BD3', '#E28AE2', '#F1F481', '#79DB80', '#DF5F5F', '#69DADE', '#C2E37D', '#E26580', '#D39F49', '#B96FE3']
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected = True)
from wordcloud import WordCloud
import country_converter as coco


df = pd.read_csv('D:/blindcat/Data_Science_Job_Salaries/ds_salaries.csv')
df.head()


# Dropping Unnecessary Columns
df.drop(df[['salary','salary_currency','Unnamed: 0']],axis=1, inplace=True)
df.head()


# Checking DF
def check_df(dataframe, head=5):

    pd.set_option('display.max_columns', None)   #*
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 170)

    print("##################### Shape #####################")
    print(dataframe.shape)

    print("##################### Info #####################")  #*
    print(dataframe.info())

    print("##################### Columns #####################")  #*
    print(dataframe.columns)

    print("##################### Types #####################")
    print(dataframe.dtypes)

    print("##################### Head #####################")
    print(dataframe.head(head))

    print("##################### Tail #####################")
    print(dataframe.tail(head))

    print("##################### NA #####################")
    print(dataframe.isnull().sum())

    print("##################### Describe #####################")
    print(dataframe.describe().T)


    check_df(df)


def missing_values(data, plot=False, target="SalePrice"):
    mst = pd.DataFrame(
        {"Num_Missing": df.isnull().sum(), "Missing_Ratio": df.isnull().sum() / df.shape[0]}).sort_values("Num_Missing",
                                                                                                          ascending=False)
    mst["DataTypes"] = df[mst.index].dtypes.values
    mst = mst[mst.Num_Missing > 0].reset_index().rename({"index": "Feature"}, axis=1)
    mst = mst[mst.Feature != target]

    print("Number of Variables include Missing Values:", mst.shape[0], "\n")

    if mst[mst.Missing_Ratio > 0.99].shape[0] > 0:
        print("Full Missing Variables:", mst[mst.Missing_Ratio > 0.99].Feature.tolist())
        data.drop(mst[mst.Missing_Ratio > 0.99].Feature.tolist(), axis=1, inplace=True)

        print("Full missing variables are deleted!", "\n")

    if plot:
        plt.figure(figsize=(25, 8))
        p = sns.barplot(mst.Feature, mst.Missing_Ratio)
        for rotate in p.get_xticklabels():
            rotate.set_rotation(90)

    print(mst, "\n")


missing_values(df)
# There is no missing values on dataset


df['experience_level'] = df['experience_level'].replace('EN','Junior')
df['experience_level'] = df['experience_level'].replace('MI','Mid-Level')
df['experience_level'] = df['experience_level'].replace('SE','Senior')
df['experience_level'] = df['experience_level'].replace('EX','Director')


def grab_col_names(dataframe, cat_th=10, car_th=20):
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]

    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]


    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary_with_graph(dataframe, col_name):
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=('Countplot', 'Percentages'),
                        specs=[[{"type": "xy"}, {'type': 'domain'}]])

    fig.add_trace(go.Bar(y=dataframe[col_name].value_counts().values.tolist(),
                         x=[str(i) for i in dataframe[col_name].value_counts().index],
                         text=dataframe[col_name].value_counts().values.tolist(),
                         textfont=dict(size=15),
                         name=col_name,
                         textposition='auto',
                         showlegend=False,
                         marker=dict(color=colors,
                                     line=dict(color='#DBE6EC',
                                               width=1))),
                  row=1, col=1)

    fig.add_trace(go.Pie(labels=dataframe[col_name].value_counts().keys(),
                         values=dataframe[col_name].value_counts().values,
                         textfont=dict(size=20),
                         textposition='auto',
                         showlegend=False,
                         name=col_name,
                         marker=dict(colors=colors)),
                  row=1, col=2)

    fig.update_layout(title={'text': col_name,
                             'y': 0.9,
                             'x': 0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'},
                      template='plotly_white')

    iplot(fig)


for col in cat_cols:
    cat_summary_with_graph(df,col)


# Which are top 5 frequent job titles?

top5_job_title = df['job_title'].value_counts()[:5]
fig = px.bar(y=top5_job_title.values, 
             x=top5_job_title.index, 
             color = top5_job_title.index,
             color_discrete_sequence=px.colors.sequential.PuBuGn,
             text=top5_job_title.values,
             title= 'Top 5 Job Titles',
             template= 'plotly_dark')
fig.update_layout(
    xaxis_title="Job Titles",
    yaxis_title="count",
    font = dict(size=17,family="Franklin Gothic"))
fig.show()


# Converting Country Names
converted_country = coco.convert(names=df['employee_residence'], to="ISO3")
df['employee_residence'] = converted_country
residence = df['employee_residence'].value_counts()


residence.head()


top10_employee_location = residence[:10]
fig = px.bar(y=top10_employee_location.values, 
             x=top10_employee_location.index, 
             color = top10_employee_location.index,
             color_discrete_sequence=px.colors.sequential.deep,
             text=top10_employee_location.values,
             title= 'Top 10 Location of Employee',
             template= 'plotly_dark')
fig.update_layout(
    xaxis_title="Location of Employee",
    yaxis_title="count",
    font = dict(size=17,family="Franklin Gothic"))
fig.show()


px.histogram(df, x = df.employee_residence.sort_values(),histnorm = 'percent', text_auto = '.1f',
             color_discrete_sequence=px.colors.qualitative.Safe,title='Count of Employee residence in each country')


text = " ".join(job_titles for job_titles in df["job_title"])
word_cloud = WordCloud(collocations = False, background_color = 'black', colormap = 'Wistia', min_font_size = 8).generate(text)
plt.figure(figsize = (10, 8))
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()


px.histogram(df, x = 'remote_ratio',color = 'work_year', barmode = 'group',color_discrete_sequence=px.colors.qualitative.Pastel,
             title='Count of each Work Type')


def num_summary_with_graph(dataframe, col_name):
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=('Quantiles', 'Distribution'))

    fig.add_trace(go.Box(y=dataframe[col_name],
                         name=str(col_name),
                         showlegend=False,
                         marker_color=colors[1]),
                  row=1, col=1)

    fig.add_trace(go.Histogram(x=dataframe[col_name],
                               xbins=dict(start=dataframe[col_name].min(),
                                          end=dataframe[col_name].max()),
                               showlegend=False,
                               name=str(col_name),
                               marker=dict(color=colors[0],
                                           line=dict(color='#DBE6EC',
                                                     width=1))),
                  row=1, col=2)

    fig.update_layout(title={'text': col_name,
                             'y': 0.9,
                             'x': 0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'},
                      template='plotly_white')

    iplot(fig)


def num_plot(data, cat_length=16, remove=["Id"], hist_bins=12, figsize=(20, 4)):
    num_cols = [col for col in data.columns if data[col].dtypes != "O"
                and len(data[col].unique()) >= cat_length]

    if len(remove) > 0:
        num_cols = list(set(num_cols).difference(remove))

    for i in num_cols:
        fig, axes = plt.subplots(1, 3, figsize=figsize)
        data.hist(str(i), bins=hist_bins, ax=axes[0])
        data.boxplot(str(i), ax=axes[1], vert=False);
        try:
            sns.kdeplot(np.array(data[str(i)]))
        except:
            ValueError

        axes[1].set_yticklabels([])
        axes[1].set_yticks([])
        axes[0].set_title(i + " | Histogram")
        axes[1].set_title(i + " | Boxplot")
        axes[2].set_title(i + " | Density")
        plt.show()


for col in num_cols:
    num_summary_with_graph(df,col)



remote_ratio = [100,50,0]

plt.figure(figsize=(20,5))
fig = px.bar(x = ['Full Remote','Half Remote','No Remote Work'], 
       y = df['remote_ratio'].value_counts().values,
       color = remote_ratio,
       color_discrete_sequence=px.colors.sequential.dense,
       text=df['remote_ratio'].value_counts().values,
       title = 'Remote Ratio Distribution',
       template='plotly_dark')

fig.update_traces(width=0.4)

fig.data[0].marker.line.width = 2


fig.update_layout(
    xaxis_title="Remote Type",
    yaxis_title="count",
    font = dict(size=17,family="Franklin Gothic"))
fig.show()


w2020 = df.loc[(df['work_year'] == 2020)]
w2021 = df.loc[(df['work_year'] == 2021)]
w2022 = df.loc[(df['work_year'] == 2022)]
hist_data = [w2020['salary_in_usd'],w2021['salary_in_usd'],w2022['salary_in_usd']]
group_labels = ['2020 salary','2021 salary','2022 salary']
colors = ['grey','black','orange']

year_salary = pd.DataFrame(columns=['2020','2021','2022'])
year_salary['2020'] = w2020.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2021'] = w2021.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2022'] = w2022.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values


fig = go.Figure(data=px.bar(x= year_salary.columns, 
                            y=year_salary.values.tolist()[0],
                            color = year_salary.columns,
                            color_discrete_sequence= colors,
                            title='Mean Salary by Work Year',
                            text = np.round([num/1000 for num in year_salary.values.tolist()[0]],2),
#                             width = [year_salary.values.tolist()[0]],
                            height=500))
fig.update_traces(width=0.3)
fig.update_layout(
    xaxis_title="Work Year",
    yaxis_title="Mean Salary (k)",
    font = dict(size=17,family="Franklin Gothic"))
fig.show()


exlevel_salary = df[['experience_level','salary_in_usd']]

entry_salary = exlevel_salary.loc[exlevel_salary['experience_level']=='Junior']
executive_salary = exlevel_salary.loc[exlevel_salary['experience_level']=='Director']
mid_salary = exlevel_salary.loc[exlevel_salary['experience_level']=='Mid-Level']
senior_salary = exlevel_salary.loc[exlevel_salary['experience_level']=='Senior']

hist_data = [entry_salary['salary_in_usd'],mid_salary['salary_in_usd'],senior_salary['salary_in_usd'],executive_salary['salary_in_usd']]
group_labels = ['Junior','Mid-level','Senior','Director']
colors = ['grey','black','orange','red']

lst = [entry_salary['salary_in_usd'].mean(),
       mid_salary['salary_in_usd'].mean(),
       senior_salary['salary_in_usd'].mean(),
       executive_salary['salary_in_usd'].mean(),]

fig2 = go.Figure(data=px.bar(x= group_labels, 
                            y=lst,
                            color = group_labels,
                            color_discrete_sequence= colors,
                            title='Mean Salary by Experience Level',
                            text = np.round([num/1000 for num in lst],2),
                            height=500))

fig2.update_traces(width=0.4)
fig2.update_layout(
    xaxis_title="Experience Level",
    yaxis_title="Mean Salary (k) ",
    font = dict(size=17,family="Franklin Gothic"))

fig2.show()


c_size = df[['company_size','salary_in_usd']]
small = exlevel_salary.loc[c_size['company_size']=='S']
mid = exlevel_salary.loc[c_size['company_size']=='M']
large = exlevel_salary.loc[c_size['company_size']=='L']
hist_data = [small['salary_in_usd'],mid['salary_in_usd'],large['salary_in_usd']]
group_labels = ['Small Company','Middle Company','Big Company']
colors = ['grey','black','orange']

lst = [small['salary_in_usd'].mean(),
       mid['salary_in_usd'].mean(),
       large['salary_in_usd'].mean()]

plt.figure(figsize=(20,5))
fig2 = go.Figure(data=px.bar(x= group_labels, 
                            y=lst,
                            color = group_labels,
                            color_discrete_sequence= colors,
                            title='Mean Salary by Company Size',
                            text = np.round([num/1000 for num in lst],2),
                            height=500))

fig2.update_traces(width=0.3)
fig2.update_layout(
    xaxis_title="Company Size",
    yaxis_title="Mean Salary (k)",
    font = dict(size=17,family="Franklin Gothic"))
fig2.show()



fig, ax = plt.subplots() 
fig.set_size_inches(20,15)
sns.heatmap(df.corr(), vmax =.9, square = True, annot = True)
plt.title('Confusion Matrix',fontsize=8,fontstyle= 'oblique')


