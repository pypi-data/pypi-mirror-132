(self.webpackChunkjupyterlab_plotly=self.webpackChunkjupyterlab_plotly||[]).push([[133,657],{133:(e,t,n)=>{"use strict";n.r(t),n.d(t,{default:()=>s});var l=n(211),i=n(657);const s={id:"jupyterlab-plotly",requires:[l.IJupyterWidgetRegistry],activate:function(e,t){t.registerWidget({name:i.o,version:i.Y,exports:()=>Promise.all([n.e(478),n.e(879)]).then(n.bind(n,879))})},autoStart:!0}},657:(e,t,n)=>{"use strict";n.d(t,{Y:()=>i,o:()=>s});const l=n(306),i=l.version,s=l.name},306:e=>{"use strict";e.exports=JSON.parse('{"name":"jupyterlab-plotly","version":"5.2.1","description":"The plotly Jupyter extension","author":"The plotly.py team","license":"MIT","main":"lib/index.js","repository":{"type":"git","url":"https://github.com/plotly/plotly.py"},"keywords":["jupyter","widgets","ipython","ipywidgets","plotly"],"files":["lib/**/*.js","dist/*.js","style/*.*"],"scripts":{"build:dev":"npm run build:lib && npm run build:nbextension && npm run build:labextension:dev","build:prod":"npm run build:lib && npm run build:nbextension && npm run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack --mode=production","clean":"npm run clean:lib && npm run clean:nbextension && npm run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf ../../python/plotly/jupyterlab_plotly/labextension","clean:nbextension":"rimraf ../../python/plotly/jupyterlab_plotly/nbextension/index.js*","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"npm run build:lib","test":"echo \\"Error: no test specified\\" && exit 1","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch"},"devDependencies":{"@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@types/plotly.js":"^1.54.10","@types/webpack-env":"^1.13.6","acorn":"^7.2.0","css-loader":"^5.2.6","fs-extra":"^7.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.0.0","webpack-cli":"^4.0.0"},"dependencies":{"@jupyter-widgets/base":"^2.0.0 || ^3.0.0 || ^4.0.0","@jupyterlab/rendermime-interfaces":"^1.3.0 || ^2.0.0 || ^3.0.0","@lumino/messaging":"^1.2.3","@lumino/widgets":"^1.8.1","lodash":"^4.17.4","plotly.js":"^2.3.1"},"jupyterlab":{"extension":"lib/jupyterlab-plugin","mimeExtension":"lib/plotly-renderer","outputDir":"../../python/plotly/jupyterlab_plotly/labextension","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}')}}]);