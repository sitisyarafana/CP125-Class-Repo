def get_legit_power_users(log_data, bot_ids, threshold):
    no_bot = {}
    for time, id, action in log_data:
        if id in bot_ids:
            continue
        
        



