# Task-4

def replace_domain(email_address, new_domain, old_domain = None):
    email_username, domain = email_address.split('@')

    if domain == new_domain:
        print('Unchanged:', email_address)
    elif domain == old_domain:
        changed_domain = email_username + '@' + new_domain
        print('Changed:', changed_domain)

replace_domain('alice@kaaj.com', 'sheba.xyz', 'kaaj.com')
replace_domain('bob@sheba.xyz', 'sheba.xyz')