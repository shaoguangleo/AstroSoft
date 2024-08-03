# Load a module only if it is not already loaded.
# If a version is specified, then switch to that version.
proc load_unless_already_loaded {pkg} {
    # puts stderr "DBG: $pkg"
    lassign [split "$pkg" /] name version
    # puts stderr "DBG: $name $version"
    # If the version isn't specified, then just check if the module is loaded.
    if { $version == "" } {
        # puts stderr "DBG: version is empty!"
        if { ! [ is-loaded "$name" ] } {
            # puts stderr "DBG: module load $name"
            module load "$name"
        }
    } else {
        # puts stderr "version is NOT empty"
        # Swap if necessary.
        if { [ is-loaded "$name" ] && ! [ is-loaded "$name/$version" ] } {
            # puts stderr "DBG: $name is loaded, but not $name/$version, so we're swapping"
            # module swap $name $name/$version # swap doesn't work???
            # puts stderr "DBG: module unload $name"
            # puts stderr "DBG: module load $name/$version"
            module unload $name
            module load $name/$version
        # Or just load the module.
        } elseif { ! [ is-loaded $name ] } {
            # puts stderr "DBG: $name is NOT loaded, so we're loading it"
            # puts stderr "module load $name/$version"
            module load $name/$version
        }
    }
}
# Load a module only if it is not already loaded.
# proc load_unless_already_loaded {name} {
#     if { ! [is-loaded $name] } {
#         module load $name
#     }
# }

# Check that the root directory actually exists.
proc fail_if_path_does_not_exist {root} {
    if { ! [file exists $root] } {
        puts stderr "$root doesn't exist! Exiting."
        exit 1
    }
}

# This function only swaps modules when:
# - $software is already loaded
# - $software/$version is not loaded.
# This means that, when loading a module of $software with a different $version
# to that already loaded, $software is unloaded first.
proc swap_module_if_version_does_not_match {software version} {
    if { [ is-loaded $software ] && ! [ is-loaded $software/$version ] } {
        module unload $software
    }
}

# All MWA software should be built with GCC 5.
#if { [is-loaded PrgEnv-cray] } {
#    module swap PrgEnv-cray PrgEnv-gnu
#    module swap gcc gcc/5.3.0
#}
#
## For zeus.
#if { [is-loaded gcc/4.8.5] } {
#    module swap gcc gcc/5.5.0
#}
#
## Conflicts.
#conflict PrgEnv-intel/5.2.82
#conflict PrgEnv-cray/5.2.82
##conflict craype-sandybridge
#conflict gcc/4.3.4
#conflict gcc/4.7.2
#conflict gcc/4.8.5
#conflict gcc/4.9.0
#conflict gcc/4.9.2
#conflict gcc/6.1.0
#conflict gcc/6.3.0
#conflict intel/13.1.1.163
#conflict intel/13.1.3.192
#conflict intel/14.0.1.106
#conflict cce/8.1.7
#conflict cce/8.1.9
#conflict cce/8.2.0
#conflict cce/8.2.3
#conflict cce/8.3.0
#conflict cce/8.3.12
#conflict cce/8.5.7

# conflict cfitsio/3.420
