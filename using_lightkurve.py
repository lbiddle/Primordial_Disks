import lightkurve as lk
# ---------------------------------------------------------------------------------------------- #
# DISPLAY THE FULL LIGHTKURVE SEARCH RESULT FOR A SPECIFIC TARGET TO VISUALIZE WHICH DATA
# PRODUCTS ARE AVAILABLE FOR THAT TARGET. 
# ---------------------------------------------------------------------------------------------- #

# ----------- SPECIFY TARGET AND MISSION ----------- #
choose_target = 'LkCa 15'
choose_mission = 'TESS'

# ----------- GENERATE AND DISPLAY SEARCH RESULT ----------- #
search_result = lk.search_lightcurve(choose_target, mission=choose_mission)
print(search_result, '\n')

# ---------------------------------------------------------------------------------------------- #
# MANY AUTHORS ARE ASSOCIATED WITH MULTIPLE MISSIONS ("SECTORS" FOR TESS, "CAMPAIGNS" FOR K2), 
# TO DOWNLOAD A LIGHTCURVE FOR A SPECIFIC AUTHOR AND MISSION, DEFINE THOSE VARIABLES AND TRUNCATE
# THE SEARCH RESULTS TABLE SO THAT IT INCLUDES ONLY THAT AUTHOR AND MISSION YOU ARE INTERESTED
# IN. EXAMPLE BELOW:
# ---------------------------------------------------------------------------------------------- #

# ----------- SPECIFY AUTHOR AND MISSION ----------- #
choose_author = 'SPOC'
choose_mission = 'TESS Sector 44'

# ----------- TRUNCATE THE SEARCH RESULT FOR SPECIFIC AUTHOR TO INCLUDE ONLY THE MISSION YOU ARE INTERESTED IN ----------- #
search_result_for_specific_author_and_mission = search_result[(search_result.mission == choose_mission) & (search_result.author == choose_author)][0]

# ----------- PRINT TRUNCATED SEARCH RESULTS TABLE TO VERIFY THAT THE CORRECT INFORMATION WAS SPECIFIED ----------- #
print(search_result_for_specific_author_and_mission, '\n')

# ----------- DOWNLOAD THE LIGHTCURVE ASSOCIATED WITH YOUR TRUNCATED SEARCH RESULTS TABLE ----------- #
lc_for_specific_author_and_mission = search_result_for_specific_author_and_mission.download()

# ---------------------------------------------------------------------------------------------- #
# THE LIGHTCURVE OBJECT CAN BE THOUGHT OF AS A TABLE TOO, AND THE CONTENT OF THE LIGHTCURVE OBJECT
# CAN VARY FROM AUTHOR TO AUTHOR. PRINT THE LIGHTCURVE OBJECT'S COLUMNS TO GAIN A CLEARER SENSE
# FOR THE EXACT DATA PRODUCTS DIFFERENT AUTHORS' LIGHTCURVE OBJECTS CONTAIN.
# ---------------------------------------------------------------------------------------------- #

# ----------- DISPLAY COLUMNS IN LIGHTCURVE OBJECT ----------- #
print(lc_for_specific_author_and_mission.columns, '\n')