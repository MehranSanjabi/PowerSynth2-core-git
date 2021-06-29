from core.MDK.LayerStack.layer_stack import Layer, LayerStack
from core.engine.InputParser.input_script import script_translator
from core.general.settings import settings


def generateLayout(layout_script, bondwire_setup, layer_stack_file):
    settings.MATERIAL_LIB_PATH = "/nethome/jgm019/testcases/tech_lib/Material/Materials.csv"  # FIXME:  Path is hardcoded.

    layer_stack = LayerStack()
    layer_stack.import_layer_stack_from_csv(layer_stack_file)

    all_layers,via_connecting_layers,cs_type_map= script_translator(input_script=layout_script, bond_wire_info=bondwire_setup, layer_stack_info=layer_stack)

    layer = all_layers[0]

    return layer.plot_init_layout(UI=True) # plotting each layer initial layout

    '''
    input_info = [layer.input_rects, layer.size, layer.origin]
    layer.new_engine.init_layout(input_format=input_info,islands=layer.new_engine.islands,all_cs_types=layer.all_cs_types,all_colors=layer.colors,bondwires=layer.bondwires)


    layer.plot_layout(fig_data=layer.new_engine.init_data[0], fig_dir="/nethome/jgm019/testcases", name="sample_name") # plots initial layout
    '''
