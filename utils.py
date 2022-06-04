def create_filter_map(filter_dict):
    '''
    Given a filter_map from streamlit, convert it into a dict supported by
    the filter_data function
    '''
    filters = {}
    for filter, value in filter_dict.items():
        if value:
            filters[filter] = value
    return filters

def filter_data(data, filters):
    if filters:
        filtered_df = data.copy()
        for key,values in filters.items():
            filtered_df = filtered_df.loc[data[key].isin(values)]
    else:
        filtered_df = data
    return filtered_df


