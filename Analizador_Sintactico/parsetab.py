
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftLESS_THANGREATER_THANLESS_EQUALGREATER_EQUALCOMPARISONNOT_EQUALleftPLUSMINUSleftTIMESDIVIDEMODULOrightPOWERrightNOTAND ARROW ASSIGN_OP BOOL COLON COMMA COMPARISON DIVIDE DOT DOUBLE ELSE FLOAT FOR FUNCTION GREATER_EQUAL GREATER_THAN IDENTIFIER IF IN INT LEFT_BRACE LEFT_BRACKET LEFT_PAREN LESS_EQUAL LESS_THAN MINUS MODULO NOT NOT_EQUAL OR PLUS POWER RETURN RIGHT_BRACE RIGHT_BRACKET RIGHT_PAREN SEMICOLON STRING TIMES TYPE_BOOL TYPE_DOUBLE TYPE_FLOAT TYPE_INTEGER TYPE_NULL TYPE_STRING TYPE_VOID WHILEprogram : statement_listdata_type : TYPE_INTEGER\n                 | TYPE_STRING\n                 | TYPE_FLOAT\n                 | TYPE_DOUBLE\n                 | TYPE_BOOL\n                 | TYPE_VOID\n                 | TYPE_NULLfactor : LEFT_PAREN expr RIGHT_PAREN\n              | IDENTIFIER\n              | INT\n              | FLOAT\n              | DOUBLE\n              | STRING\n              | BOOL\n              | NOT expr\n              | expr COMPARISON expr\n              | expr LESS_THAN expr\n              | expr GREATER_THAN expr\n              | expr LESS_EQUAL expr\n              | expr GREATER_EQUAL expr\n              | expr NOT_EQUAL expr\n              | expr AND expr\n              | expr OR exprexpr : expr PLUS factor\n            | expr MINUS factor\n            | expr TIMES factor\n            | expr DIVIDE factor\n            | expr MODULO factor\n            | expr POWER factor\n            | factorvar_decl : IDENTIFIER COLON data_type ASSIGN_OP exprparam_list : param_list COMMA IDENTIFIER COLON data_type\n                  | IDENTIFIER COLON data_type\n                  | emptystatement_list : statement_list statement\n                      | emptystatement : expr SEMICOLON\n                 | return_statement SEMICOLON \n                 | var_decl SEMICOLON\n                 | var_reassign SEMICOLON\n                 | if_statement\n                 | while_statement \n                 | for_statement\n                 | func_decl\n                 | blockblock : LEFT_BRACE statement_list RIGHT_BRACEif_statement : IF LEFT_PAREN expr RIGHT_PAREN block\n                    | IF LEFT_PAREN expr RIGHT_PAREN block ELSE blockwhile_statement : WHILE LEFT_PAREN expr RIGHT_PAREN blockfor_statement : FOR IDENTIFIER IN IDENTIFIER blockreturn_statement : RETURN exprfunc_decl : FUNCTION IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN ARROW data_type blockempty :var_reassign : IDENTIFIER ASSIGN_OP expr'
    
_lr_action_items = {'RETURN':([0,2,3,4,9,10,11,12,13,22,29,44,45,46,56,87,96,97,98,106,109,],[-54,15,-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,15,-47,-48,-50,-51,-49,-53,]),'IDENTIFIER':([0,2,3,4,9,10,11,12,13,15,18,20,21,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,85,86,87,88,96,97,98,101,106,109,],[-54,16,-37,-36,-42,-43,-44,-45,-46,48,48,54,55,-54,48,-38,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-39,-40,-41,48,48,48,16,91,92,-47,48,-48,-50,-51,105,-49,-53,]),'IF':([0,2,3,4,9,10,11,12,13,22,29,44,45,46,56,87,96,97,98,106,109,],[-54,17,-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,17,-47,-48,-50,-51,-49,-53,]),'WHILE':([0,2,3,4,9,10,11,12,13,22,29,44,45,46,56,87,96,97,98,106,109,],[-54,19,-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,19,-47,-48,-50,-51,-49,-53,]),'FOR':([0,2,3,4,9,10,11,12,13,22,29,44,45,46,56,87,96,97,98,106,109,],[-54,20,-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,20,-47,-48,-50,-51,-49,-53,]),'FUNCTION':([0,2,3,4,9,10,11,12,13,22,29,44,45,46,56,87,96,97,98,106,109,],[-54,21,-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,21,-47,-48,-50,-51,-49,-53,]),'LEFT_BRACE':([0,2,3,4,9,10,11,12,13,22,29,44,45,46,56,74,75,76,77,78,79,80,87,89,90,91,96,97,98,102,106,107,109,],[-54,22,-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,22,-2,-3,-4,-5,-6,-7,-8,-47,22,22,22,-48,-50,-51,22,-49,22,-53,]),'LEFT_PAREN':([0,2,3,4,9,10,11,12,13,15,17,18,19,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,55,56,87,88,96,97,98,106,109,],[-54,18,-37,-36,-42,-43,-44,-45,-46,18,51,18,53,-54,18,-38,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-39,-40,-41,18,18,18,86,18,-47,18,-48,-50,-51,-49,-53,]),'INT':([0,2,3,4,9,10,11,12,13,15,18,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,87,88,96,97,98,106,109,],[-54,23,-37,-36,-42,-43,-44,-45,-46,23,23,-54,23,-38,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-39,-40,-41,23,23,23,23,-47,23,-48,-50,-51,-49,-53,]),'FLOAT':([0,2,3,4,9,10,11,12,13,15,18,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,87,88,96,97,98,106,109,],[-54,24,-37,-36,-42,-43,-44,-45,-46,24,24,-54,24,-38,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-39,-40,-41,24,24,24,24,-47,24,-48,-50,-51,-49,-53,]),'DOUBLE':([0,2,3,4,9,10,11,12,13,15,18,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,87,88,96,97,98,106,109,],[-54,25,-37,-36,-42,-43,-44,-45,-46,25,25,-54,25,-38,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-39,-40,-41,25,25,25,25,-47,25,-48,-50,-51,-49,-53,]),'STRING':([0,2,3,4,9,10,11,12,13,15,18,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,87,88,96,97,98,106,109,],[-54,26,-37,-36,-42,-43,-44,-45,-46,26,26,-54,26,-38,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-39,-40,-41,26,26,26,26,-47,26,-48,-50,-51,-49,-53,]),'BOOL':([0,2,3,4,9,10,11,12,13,15,18,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,87,88,96,97,98,106,109,],[-54,27,-37,-36,-42,-43,-44,-45,-46,27,27,-54,27,-38,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-39,-40,-41,27,27,27,27,-47,27,-48,-50,-51,-49,-53,]),'NOT':([0,2,3,4,9,10,11,12,13,15,18,22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,51,53,56,87,88,96,97,98,106,109,],[-54,28,-37,-36,-42,-43,-44,-45,-46,28,28,-54,28,-38,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-39,-40,-41,28,28,28,28,-47,28,-48,-50,-51,-49,-53,]),'$end':([0,1,2,3,4,9,10,11,12,13,29,44,45,46,87,96,97,98,106,109,],[-54,0,-1,-37,-36,-42,-43,-44,-45,-46,-38,-39,-40,-41,-47,-48,-50,-51,-49,-53,]),'RIGHT_BRACE':([3,4,9,10,11,12,13,22,29,44,45,46,56,87,96,97,98,106,109,],[-37,-36,-42,-43,-44,-45,-46,-54,-38,-39,-40,-41,87,-47,-48,-50,-51,-49,-53,]),'SEMICOLON':([5,6,7,8,14,16,23,24,25,26,27,47,48,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,83,95,],[29,44,45,46,-31,-10,-11,-12,-13,-14,-15,-52,-10,-16,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,-23,-24,-55,-9,-32,]),'PLUS':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[30,-31,-10,-11,-12,-13,-14,-15,30,-10,30,-16,30,-25,-26,-27,-28,-29,-30,30,30,30,30,30,30,30,30,30,30,-9,30,30,]),'MINUS':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[31,-31,-10,-11,-12,-13,-14,-15,31,-10,31,-16,31,-25,-26,-27,-28,-29,-30,31,31,31,31,31,31,31,31,31,31,-9,31,31,]),'TIMES':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[32,-31,-10,-11,-12,-13,-14,-15,32,-10,32,-16,32,-25,-26,-27,-28,-29,-30,32,32,32,32,32,32,32,32,32,32,-9,32,32,]),'DIVIDE':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[33,-31,-10,-11,-12,-13,-14,-15,33,-10,33,-16,33,-25,-26,-27,-28,-29,-30,33,33,33,33,33,33,33,33,33,33,-9,33,33,]),'MODULO':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[34,-31,-10,-11,-12,-13,-14,-15,34,-10,34,-16,34,-25,-26,-27,-28,-29,-30,34,34,34,34,34,34,34,34,34,34,-9,34,34,]),'POWER':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[35,-31,-10,-11,-12,-13,-14,-15,35,-10,35,-16,35,-25,-26,-27,-28,-29,-30,35,35,35,35,35,35,35,35,35,35,-9,35,35,]),'COMPARISON':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[36,-31,-10,-11,-12,-13,-14,-15,36,-10,36,-16,36,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,36,36,36,36,-9,36,36,]),'LESS_THAN':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[37,-31,-10,-11,-12,-13,-14,-15,37,-10,37,-16,37,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,37,37,37,37,-9,37,37,]),'GREATER_THAN':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[38,-31,-10,-11,-12,-13,-14,-15,38,-10,38,-16,38,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,38,38,38,38,-9,38,38,]),'LESS_EQUAL':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[39,-31,-10,-11,-12,-13,-14,-15,39,-10,39,-16,39,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,39,39,39,39,-9,39,39,]),'GREATER_EQUAL':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[40,-31,-10,-11,-12,-13,-14,-15,40,-10,40,-16,40,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,40,40,40,40,-9,40,40,]),'NOT_EQUAL':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[41,-31,-10,-11,-12,-13,-14,-15,41,-10,41,-16,41,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,41,41,41,41,-9,41,41,]),'AND':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[42,-31,-10,-11,-12,-13,-14,-15,42,-10,42,-16,42,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,-23,42,42,42,-9,42,42,]),'OR':([5,14,16,23,24,25,26,27,47,48,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,81,82,83,84,95,],[43,-31,-10,-11,-12,-13,-14,-15,43,-10,43,-16,43,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,-23,-24,43,43,-9,43,43,]),'RIGHT_PAREN':([14,23,24,25,26,27,48,52,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,76,77,78,79,80,82,83,84,86,93,94,103,110,],[-31,-11,-12,-13,-14,-15,-10,83,-16,-25,-26,-27,-28,-29,-30,-17,-18,-19,-20,-21,-22,-23,-24,-2,-3,-4,-5,-6,-7,-8,89,-9,90,-54,100,-35,-34,-33,]),'COLON':([16,92,105,],[49,99,108,]),'ASSIGN_OP':([16,73,74,75,76,77,78,79,80,],[50,88,-2,-3,-4,-5,-6,-7,-8,]),'TYPE_INTEGER':([49,99,104,108,],[74,74,74,74,]),'TYPE_STRING':([49,99,104,108,],[75,75,75,75,]),'TYPE_FLOAT':([49,99,104,108,],[76,76,76,76,]),'TYPE_DOUBLE':([49,99,104,108,],[77,77,77,77,]),'TYPE_BOOL':([49,99,104,108,],[78,78,78,78,]),'TYPE_VOID':([49,99,104,108,],[79,79,79,79,]),'TYPE_NULL':([49,99,104,108,],[80,80,80,80,]),'IN':([54,],[85,]),'COMMA':([74,75,76,77,78,79,80,86,93,94,103,110,],[-2,-3,-4,-5,-6,-7,-8,-54,101,-35,-34,-33,]),'ELSE':([87,96,],[-47,102,]),'ARROW':([100,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,22,],[2,56,]),'empty':([0,22,86,],[3,3,94,]),'statement':([2,56,],[4,4,]),'expr':([2,15,18,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,50,51,53,56,88,],[5,47,52,57,58,58,58,58,58,58,65,66,67,68,69,70,71,72,81,82,84,5,95,]),'return_statement':([2,56,],[6,6,]),'var_decl':([2,56,],[7,7,]),'var_reassign':([2,56,],[8,8,]),'if_statement':([2,56,],[9,9,]),'while_statement':([2,56,],[10,10,]),'for_statement':([2,56,],[11,11,]),'func_decl':([2,56,],[12,12,]),'block':([2,56,89,90,91,102,107,],[13,13,96,97,98,106,109,]),'factor':([2,15,18,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,50,51,53,56,88,],[14,14,14,14,59,60,61,62,63,64,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'data_type':([49,99,104,108,],[73,103,107,110,]),'param_list':([86,],[93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','analizador_sintactico.py',21),
  ('data_type -> TYPE_INTEGER','data_type',1,'p_data_type','analizador_sintactico.py',26),
  ('data_type -> TYPE_STRING','data_type',1,'p_data_type','analizador_sintactico.py',27),
  ('data_type -> TYPE_FLOAT','data_type',1,'p_data_type','analizador_sintactico.py',28),
  ('data_type -> TYPE_DOUBLE','data_type',1,'p_data_type','analizador_sintactico.py',29),
  ('data_type -> TYPE_BOOL','data_type',1,'p_data_type','analizador_sintactico.py',30),
  ('data_type -> TYPE_VOID','data_type',1,'p_data_type','analizador_sintactico.py',31),
  ('data_type -> TYPE_NULL','data_type',1,'p_data_type','analizador_sintactico.py',32),
  ('factor -> LEFT_PAREN expr RIGHT_PAREN','factor',3,'p_factor','analizador_sintactico.py',37),
  ('factor -> IDENTIFIER','factor',1,'p_factor','analizador_sintactico.py',38),
  ('factor -> INT','factor',1,'p_factor','analizador_sintactico.py',39),
  ('factor -> FLOAT','factor',1,'p_factor','analizador_sintactico.py',40),
  ('factor -> DOUBLE','factor',1,'p_factor','analizador_sintactico.py',41),
  ('factor -> STRING','factor',1,'p_factor','analizador_sintactico.py',42),
  ('factor -> BOOL','factor',1,'p_factor','analizador_sintactico.py',43),
  ('factor -> NOT expr','factor',2,'p_factor','analizador_sintactico.py',44),
  ('factor -> expr COMPARISON expr','factor',3,'p_factor','analizador_sintactico.py',45),
  ('factor -> expr LESS_THAN expr','factor',3,'p_factor','analizador_sintactico.py',46),
  ('factor -> expr GREATER_THAN expr','factor',3,'p_factor','analizador_sintactico.py',47),
  ('factor -> expr LESS_EQUAL expr','factor',3,'p_factor','analizador_sintactico.py',48),
  ('factor -> expr GREATER_EQUAL expr','factor',3,'p_factor','analizador_sintactico.py',49),
  ('factor -> expr NOT_EQUAL expr','factor',3,'p_factor','analizador_sintactico.py',50),
  ('factor -> expr AND expr','factor',3,'p_factor','analizador_sintactico.py',51),
  ('factor -> expr OR expr','factor',3,'p_factor','analizador_sintactico.py',52),
  ('expr -> expr PLUS factor','expr',3,'p_expr','analizador_sintactico.py',62),
  ('expr -> expr MINUS factor','expr',3,'p_expr','analizador_sintactico.py',63),
  ('expr -> expr TIMES factor','expr',3,'p_expr','analizador_sintactico.py',64),
  ('expr -> expr DIVIDE factor','expr',3,'p_expr','analizador_sintactico.py',65),
  ('expr -> expr MODULO factor','expr',3,'p_expr','analizador_sintactico.py',66),
  ('expr -> expr POWER factor','expr',3,'p_expr','analizador_sintactico.py',67),
  ('expr -> factor','expr',1,'p_expr','analizador_sintactico.py',68),
  ('var_decl -> IDENTIFIER COLON data_type ASSIGN_OP expr','var_decl',5,'p_var_decl','analizador_sintactico.py',76),
  ('param_list -> param_list COMMA IDENTIFIER COLON data_type','param_list',5,'p_param_list','analizador_sintactico.py',82),
  ('param_list -> IDENTIFIER COLON data_type','param_list',3,'p_param_list','analizador_sintactico.py',83),
  ('param_list -> empty','param_list',1,'p_param_list','analizador_sintactico.py',84),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','analizador_sintactico.py',94),
  ('statement_list -> empty','statement_list',1,'p_statement_list','analizador_sintactico.py',95),
  ('statement -> expr SEMICOLON','statement',2,'p_statement','analizador_sintactico.py',103),
  ('statement -> return_statement SEMICOLON','statement',2,'p_statement','analizador_sintactico.py',104),
  ('statement -> var_decl SEMICOLON','statement',2,'p_statement','analizador_sintactico.py',105),
  ('statement -> var_reassign SEMICOLON','statement',2,'p_statement','analizador_sintactico.py',106),
  ('statement -> if_statement','statement',1,'p_statement','analizador_sintactico.py',107),
  ('statement -> while_statement','statement',1,'p_statement','analizador_sintactico.py',108),
  ('statement -> for_statement','statement',1,'p_statement','analizador_sintactico.py',109),
  ('statement -> func_decl','statement',1,'p_statement','analizador_sintactico.py',110),
  ('statement -> block','statement',1,'p_statement','analizador_sintactico.py',111),
  ('block -> LEFT_BRACE statement_list RIGHT_BRACE','block',3,'p_block','analizador_sintactico.py',116),
  ('if_statement -> IF LEFT_PAREN expr RIGHT_PAREN block','if_statement',5,'p_if_statement','analizador_sintactico.py',121),
  ('if_statement -> IF LEFT_PAREN expr RIGHT_PAREN block ELSE block','if_statement',7,'p_if_statement','analizador_sintactico.py',122),
  ('while_statement -> WHILE LEFT_PAREN expr RIGHT_PAREN block','while_statement',5,'p_while_statement','analizador_sintactico.py',130),
  ('for_statement -> FOR IDENTIFIER IN IDENTIFIER block','for_statement',5,'p_for_statement','analizador_sintactico.py',135),
  ('return_statement -> RETURN expr','return_statement',2,'p_return_statement','analizador_sintactico.py',140),
  ('func_decl -> FUNCTION IDENTIFIER LEFT_PAREN param_list RIGHT_PAREN ARROW data_type block','func_decl',8,'p_func_decl','analizador_sintactico.py',145),
  ('empty -> <empty>','empty',0,'p_empty','analizador_sintactico.py',150),
  ('var_reassign -> IDENTIFIER ASSIGN_OP expr','var_reassign',3,'p_var_reassign','analizador_sintactico.py',154),
]
