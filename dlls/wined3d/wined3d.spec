@ stdcall WineDirect3DCreateClipper()
@ stdcall wined3d_mutex_lock()
@ stdcall wined3d_mutex_unlock()

@ cdecl wined3d_check_depth_stencil_match(ptr long long long long long)
@ cdecl wined3d_check_device_format(ptr long long long long long long long)
@ cdecl wined3d_check_device_format_conversion(ptr long long long long)
@ cdecl wined3d_check_device_multisample_type(ptr long long long long long ptr)
@ cdecl wined3d_check_device_type(ptr long long long long long)
@ cdecl wined3d_create(long ptr)
@ cdecl wined3d_decref(ptr)
@ cdecl wined3d_enum_adapter_modes(ptr long long long ptr)
@ cdecl wined3d_get_adapter_count(ptr)
@ cdecl wined3d_get_adapter_display_mode(ptr long ptr)
@ cdecl wined3d_get_adapter_identifier(ptr long long ptr)
@ cdecl wined3d_get_adapter_mode_count(ptr long long)
@ cdecl wined3d_get_adapter_monitor(ptr long)
@ cdecl wined3d_get_device_caps(ptr long long ptr)
@ cdecl wined3d_get_parent(ptr)
@ cdecl wined3d_incref(ptr)
@ cdecl wined3d_register_software_device(ptr ptr);

@ cdecl wined3d_device_create(ptr long long ptr long ptr ptr);

@ cdecl wined3d_stateblock_apply(ptr)
@ cdecl wined3d_stateblock_capture(ptr)
@ cdecl wined3d_stateblock_decref(ptr)
@ cdecl wined3d_stateblock_incref(ptr)
