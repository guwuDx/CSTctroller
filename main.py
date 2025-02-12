from utils import misc
from utils import cst_general
from utils import basic_operations
from utils import materials_operations
from utils import param_operations
from utils.macors_canva import Canvas

import pythoncom
pythoncom.CoInitialize()

def main():

    print("<<<<<<<<<<<<<<< CST Automation >>>>>>>>>>>>>>>")
    cst = cst_general.CSTHandler(debug=True)
    cst.open_template("SquarePillar")
    cst.instantiate_template("SquarePillar_inst", 10, 10.5)
    basic_operations.define_material(cst, "materials", "freq-r-i_Si_crystal_0.0310-310um_ByFranta-300K_2017")
    materials_operations.SquarePillar(cst).change_substrate("freq-r-i_Si_crystal_0.0310-310um_ByFranta-300K_2017")
    materials_operations.SquarePillar(cst).change_pillar("freq-r-i_Si_crystal_0.0310-310um_ByFranta-300K_2017")
    # basic_operations.modify_param(cst_app=cst, param_name="p", value=10)
    basic_operations.set_acc_dc(cst)
    basic_operations.set_FDSolver_source(cst, "Zmin", "TM(0,0)")
    canvas = Canvas()

    ps = param_operations.SquarePillar(cst)
    ps.generate_sweep_squence(0.5, 0.5, 0.5)
    ps.set_sweep_from_list(cst, distributed=True, start_now=True)

    # cst.close()
    print("Done")


if __name__ == '__main__':
    main()