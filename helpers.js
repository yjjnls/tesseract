Module['preInit'] = function(){
    FS.mkdir('/WD');
    FS.mount(NODEFS, { root: '.' }, '/WD');
    console.log("+++++++++++++++++++++++++++")
}