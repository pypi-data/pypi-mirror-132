function initializeOpenRASP() {
    // These require statements initializes the open-rasp with their official plugin
    // global.RASP object is created which is to be used for further interaction
    require('./flex');
    require('../../../../addons/third_party/openrasp/openrasp-v8/base/js/rasp')

    // Disable console.log to supress log info from open-rasp initialization
    const originalLogger = console.log;
    console.log = (() => { });
    require('../../../../addons/third_party/openrasp/plugins/official/plugin');
    console.log = originalLogger;
}

module.exports = initializeOpenRASP;
