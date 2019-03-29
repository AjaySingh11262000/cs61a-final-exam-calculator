def minimum_score(mt1_score, mt2_score, desired_grade, ec_points = 0, recovery_points = 0):
    grade_bins = {'A+':0, 'A':15,'A-':30,'B+':50,'B':75,'B-':95,'C+':105,'C':115,'C-':125,'D+':130,'D':135,'D-':140} # max points that can be lost for each letter grade 
    assert desired_grade in grade_bins, "Your desired_grade must be an uppercase string. For example,'b+' should be inputted as 'B+'" 
    assert mt1_score <= 30 and mt2_score <= 60, 'mt1_score and mt2_score should be ints or floats that are less than 30 and 60, respectively'
    list_of_scenario_outcomes = []
    max_points_missed = grade_bins[desired_grade] + ec_points + recovery_points
    
    #scenario 1: assumes no clobbering necessary:
    for i in reversed(range(76)):
        if ((75-i)+(30-mt1_score)+(60-mt2_score)) >= max_points_missed or i == 0 :
            list_of_scenario_outcomes.append(i)
            break
            
    #scenario 2: assumes mt1 is being clobbered:
    for i in reversed(range(76)):
        if ((75-i) + (30-((i/75)*30)) + (60-mt2_score)) >= max_points_missed or i == 0:
            list_of_scenario_outcomes.append(i)
            break
            
    #scenario 3: assumes mt2 is being clobbered:
    for i in reversed(range(76)):
        if ((75-i) + (60-((i/75)*60)) + (30-mt1_score)) >= max_points_missed or i == 0:
            list_of_scenario_outcomes.append(i)
            break
    
    #scenario 4: assumes BOTH midterms are being clobbered:
    for i in reversed(range(76)):
        if ((75-i) + (30-((i/75)*30)) + (60-((i/75)*60))) >= max_points_missed or i == 0:
            list_of_scenario_outcomes.append(i)
            break
            
    score_needed = min(list_of_scenario_outcomes)
    print('_____________')
    print('The minimum score you need on the final exam to earn a(n) ' + desired_grade + ' in CS61A is:' )
    print('\n'+str(score_needed) + ' out of 75')
    print('\nKeep in mind that this calculator does not take into account any beneficial grade bin shifts \nthat may occur at the end, and that there are still 4-5 EC points left in the semester.')
    print('_____________ \n made by shoumik :D')

