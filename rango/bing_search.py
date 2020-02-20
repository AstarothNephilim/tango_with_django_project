import json
import requests

def read_bing_key():
    """
    reads the BING API key frim a file called 'bing.key'
    returns: a string which is either None, i.e no key found, or with a key
    """
    bing_api_key = None
    try:
        with open('bing.key.txt','r') as f:
            bing_api_key = f.readline().strip()
    except:
        try:
            with open('../bing.key.txt') as f:
                bing_api_key = f.readline().strip()
        except:
            raise IOError('bing.key file not found')
    
    if not bing_api_key:
        raise KeyError('Bing key not found')
        
    return bing_api_key

def run_query(search_terms):
    """
    See Microsoft docum for other parameters http://bit.ly/twd-bing-api
    """
    bing_key = read_bing_key()
    search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_key}
    params = {'q': search_terms, 'textDecorations': True, 'textFormat':'HTML'}
    
    #Issue the request, given the details above.
    try:
        response = requests.get(search_url, headers = headers, params = params)
        response.raise_for_status()
        search_results = response.json()
    except:
        raise NameError("This can't be found")
    
    #With response now in play build a python list
    results = []
    for result in search_results['webPages']['value']:
        results.append({
            'title':result['name'],
            'link': result['url'],
            'summary': result['snippet']})
    return results
    
def main():
    query = input('Enter your search: \n')
    run_query(query)
     
if __name__ == '__main__':
    main()
    
    

    
