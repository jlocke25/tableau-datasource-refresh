import tableauserverclient as TSC
import sys
from acon import tableau

#Create Tableau Server Connnection Process
class TableauServerConnection:
    def __init__(self, server_url, token_name, token_secret, site):
        self.server_url = server_url
        self.token_name = token_name
        self.token_secret = token_secret
        self.site = site

    def to_string(self):
        print("server_url={}\ntoken_name={}\ntoken_secret={}\nsite={}".format( self.server_url
                                                                              ,self.token_name
                                                                              ,self.token_secret
                                                                              ,self.site))
#Create Refresh Data Source Process
def refreshDataSourceTableauServer(myTSConnection, datasource_id):
    server = TSC.Server(myTSConnection.server_url, use_server_version=True)
    tableau_auth = TSC.PersonalAccessTokenAuth(token_name=myTSConnection.token_name
                                               ,personal_access_token=myTSConnection.token_secret
                                               ,site_id=myTSConnection.site)
    with server.auth.sign_in_with_personal_access_token(tableau_auth):
        print('[Logged in successfully to {}]'.format(myTSConnection.server_url))
        
        datasource = server.datasources.get_by_id(datasource_id)
        print('[Datasource previusly updated at {}]'.format(datasource.updated_at))
        refreshed_datasource = server.datasources.refresh(datasource)
        
        print('[Datasource {} refreshed]'.format(datasource.name))

#Create connection to Tableau Server using parameters from config.py
tsConn = TableauServerConnection(tableau.prod_msc.url,tableau.prod_msc.token_name,tableau.prod_msc.token, tableau.prod_msc.site)


if len(sys.argv) != 2:
    raise ValueError('No datasource argument provided')

#Call data refresh procedure with LUID from the Tableau DataSource.  This can be found in the PostgreSQL table 'datasources'
#or you can just simply query this view and pass the exact DataSource name... SELECT ds_luid FROM [Common].[dbo].[vw_Tableau_PublishedDataSources] WHERE ds_name = 'XXXXXXXXXXXXXX'
refreshDataSourceTableauServer(tsConn, sys.argv[1])
