const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
// })

module.exports = {
    devServer: {
        proxy: 'http://127.0.0.1:5000/',
    }
}


// module.exports = {
//     devServer: {
//         proxy: {
//             '^/api': {
//                 target: 'http://127.0.0.1:5000/',//接口的前缀
//                 ws:true,//代理websocked
//                 changeOrigin:true,//虚拟的站点需要更管origin
//                 secure: true,
//                 pathRewrite:{
//                     '^/api/detail':'/api/detail'//重写路径
//                 }
//             }
//         }
//     }
// }
