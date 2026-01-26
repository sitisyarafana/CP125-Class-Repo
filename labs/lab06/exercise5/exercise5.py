def audit_zero_trust(baseline_set, current_log_list):
    log_list = set(current_log_list)
    authorized = log_list & baseline_set
    alerts =  log_list - baseline_set
    inactive =  baseline_set - log_list
    return (authorized, alerts, inactive)