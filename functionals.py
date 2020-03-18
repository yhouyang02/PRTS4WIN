import pandas as pd

# Returns exp needed
def exp_needed(op_leveli, op_levelf, elite_level):
	exp = 0
	# import exp data from Excel Database (local)
	# Ref: http://ak.mooncell.wiki/w/%E6%B8%B8%E6%88%8F%E6%95%B0%E6%8D%AE%E5%9F%BA%E7%A1%80#.E5.90.84.E7.AD.89.E7.BA.A7.E5.AF.B9.E5.BA.94.E7.BB.8F.E9.AA.8C.E5.80.BC
	exp_data = pd.read_excel('data.xlsx', sheet_name='cumulative_exp')
	CUMULATIVE_EXP_ELITE0 = list(exp_data['Elite0'])
	CUMULATIVE_EXP_ELITE1 = list(exp_data['Elite1'])
	CUMULATIVE_EXP_ELITE2 = list(exp_data['Elite2'])
	if elite_level == 0:
		exp = (int)(CUMULATIVE_EXP_ELITE0[op_levelf-1]) - (int)(CUMULATIVE_EXP_ELITE0[op_leveli-1])
	elif elite_level == 1:
		exp = (int)(CUMULATIVE_EXP_ELITE1[op_levelf-1]) - (int)(CUMULATIVE_EXP_ELITE1[op_leveli-1])
	elif elite_level == 2:
		exp = (int)(CUMULATIVE_EXP_ELITE2[op_levelf-1]) - (int)(CUMULATIVE_EXP_ELITE2[op_leveli-1])
	else:
		exp = -999 # error code
	return exp

# Returns lmd needed
def lmd_needed(op_leveli, op_levelf, elite_level):
	lmd = 0
	# import lmd data from Excel Database (local)
	# Ref: http://ak.mooncell.wiki/w/%E6%B8%B8%E6%88%8F%E6%95%B0%E6%8D%AE%E5%9F%BA%E7%A1%80#.E5.90.84.E7.AD.89.E7.BA.A7.E5.AF.B9.E5.BA.94.E7.BB.8F.E9.AA.8C.E5.80.BC
	lmd_data = pd.read_excel('data.xlsx', sheet_name='cumulative_lmd')
	CUMULATIVE_LMD_ELITE0 = list(lmd_data['Elite0'])
	CUMULATIVE_LMD_ELITE1 = list(lmd_data['Elite1'])
	CUMULATIVE_LMD_ELITE2 = list(lmd_data['Elite2'])
	if elite_level == 0:
		lmd = (int)(CUMULATIVE_LMD_ELITE0[op_levelf-1]) - (int)(CUMULATIVE_LMD_ELITE0[op_leveli-1])
	elif elite_level == 1:
		lmd = (int)(CUMULATIVE_LMD_ELITE1[op_levelf-1]) - (int)(CUMULATIVE_LMD_ELITE1[op_leveli-1])
	elif elite_level == 2:
		lmd = (int)(CUMULATIVE_LMD_ELITE2[op_levelf-1]) - (int)(CUMULATIVE_LMD_ELITE2[op_leveli-1])
	else:
		lmd = -999 # error code
	return lmd

# Returns number of Strategic BR needed for upload
def stra_br_needed(op_leveli, op_levelf, elite_level):
	EXP_STRAGETIC_BATTLE_RECORD = 2000 # constant exp provided by a Strategic BR
	return exp / EXP_STRAGETIC_BATTLE_RECORD