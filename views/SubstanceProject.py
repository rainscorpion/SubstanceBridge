import bpy


# -----------------------------------------------------------------------------
# Substance Project panel
# -----------------------------------------------------------------------------
class SubstanceProjectPanel(bpy.types.Panel):
    bl_label = "Substance Project"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Substances"

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        layout.label("Project Name")
        row = layout.row(align=True)
        icon = "GROUP"
        row.prop(scn, 'project_name', text="", icon=icon)
        icon = "ZOOMIN"
        row.operator("painter.substance_name", text="", icon=icon)
        icon = "RESTRICT_SELECT_OFF"
        row.operator("painter.selected_project", text="", icon=icon)

        name = "New Project"
        layout.operator("object.painter_export", name).project = False

        type_file = 'sppfile'
        layout.prop(context.scene, type_file, text="")

        name = 'Update'
        layout.operator("object.painter_export", name).project = True


def register():
    bpy.utils.register_class(SubstanceProjectPanel)


def unregister():
    bpy.utils.unregister_class(SubstanceProjectPanel)