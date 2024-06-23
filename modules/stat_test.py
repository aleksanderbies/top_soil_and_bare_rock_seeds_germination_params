from scipy.stats import ttest_ind, mannwhitneyu

def tStudent_test(s1, s2):
    stat, p_value = ttest_ind(s1, s2)

    print("Student's t-test for two independent samples:")
    print("Test statistic value:", stat)
    print("p value:", p_value)
    if p_value > 0.05:
        print("There are no grounds to reject the null hypothesis - no significant difference between the groups.")
    else:
        print("We reject the null hypothesis - there is a significant difference between the groups.")
        
def Mann_Whitney_U_test(s1, s2):
    stat, p_value = mannwhitneyu(s1, s2)

    print("Mann Whitney U test for two independent samples:")
    print("Test statistic value:", stat)
    print("p value:", p_value)
    if p_value > 0.05:
        print("There are no grounds to reject the null hypothesis - no significant difference between the groups.")
    else:
        print("We reject the null hypothesis - there is a significant difference between the groups.")