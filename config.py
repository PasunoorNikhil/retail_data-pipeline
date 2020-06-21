"""Source and target Data base details can be changed here"""
DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_HOST': '34.72.91.74',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user',
            'DB_PASS': 'your password for source db'
        },
        'TARGET_DB': {
            'DB_HOST': '34.72.91.74',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user',
            'DB_PASS': 'your password for target db'
        }
    },
    'testing': {
        'SOURCE_DB': {
            'DB_HOST': 'Enter Testing source db_host',
            'DB_NAME': 'Enter Testing source db_name',
            'DB_USER': 'Enter Testing source db_user',
            'DB_PASS': 'Enter Testing source db_pass'
        },
        'TARGET_DB': {
            'DB_HOST': 'Enter Testing target db_host',
            'DB_NAME': 'Enter Testing target db_name',
            'DB_USER': 'Enter Testing target db_user',
            'DB_PASS': 'Enter Testing target db_pass'
        }
    }
}
