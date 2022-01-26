(async () => {
    var res = await request({ url: '/v1/data/everyMonthPublishNum' })
    var xAxisLabel = []
    for (let i = 0; i < res['xAxis'].length; i++) {
        xAxisLabel.push(`${res['xAxis'][i]}月`)
    }
    // 实例化对象
    const everyMonthPublishNum = echarts.init(document.getElementById('everyMonthPublishNum'));
    everyMonthPublishNum.setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '2%',
            bottom: '2%',
            top: '15%',
            containLabel: true,
            // backgroundColor: #fff
        },
        xAxis: {
            type: 'category',
            data: xAxisLabel,
            name: '时间',
            // offset: 25,
            axisLabel: {
                // interval: 0,
                // rotate: 40,
                align: 'center',
                textStyle: {
                    color: '#fff'
                },
            },
            grid: {
                left: '10%',
                bottom: '35%'
            },
            textStyle: {
                color: '#fff'
            },
        },
        yAxis: {
            name: '数量 单位: 千（本）',
            type: 'value',
            nameTextStyle: {
                // 坐标轴名称样式
                color: '#fff',
                padding: [0, 0, 0, 60] // 坐标轴名称相对位置
            },
            axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                formatter: function (value) {
                    if (value > 10000) {
                        return value / 10000 + 'w'
                    } else if (value > 0) {
                        return (value / 1000).toFixed(1) + 'k'
                    } else {
                        return value
                    }
                }
            }
        },
        dataZoom: [
            {
                type: 'inside'
            }
        ],
        series: [
            {
                data: res['yAxis'],
                type: 'line',
                smooth: true
            }
        ]
    });
})();
// // 指定配置和数据
// everyMonthPublishNum.setOption({
//     tooltip: {
//         trigger: 'axis',
//         axisPointer: {
//             type: 'shadow'
//         }
//     },
//     grid: {
//         left: '3%',
//         right: '2%',
//         bottom: '2%',
//         top: '15%',
//         containLabel: true,
//         // backgroundColor: #fff
//     },
//     xAxis: {
//         type: 'category',
//         // data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
//         name: '时间',
//         // offset: 25,
//         axisLabel: {
//             // interval: 0,
//             // rotate: 40,
//             align: 'center',
//             textStyle: {
//                 color: '#fff'
//             },
//         },
//         grid: {
//             left: '10%',
//             bottom: '35%'
//         },
//         textStyle: {
//             color: '#fff'
//         },
//     },
//     yAxis: {
//         name: '数量 单位: 千（本）',
//         type: 'value',
//         nameTextStyle: {
//             // 坐标轴名称样式
//             color: '#fff',
//             padding: [0, 0, 0, 60] // 坐标轴名称相对位置
//         },
//         axisLabel: {
//             textStyle: {
//                 color: '#fff'
//             },
//             formatter: function (value) {
//                 if (value > 10000) {
//                     return value / 10000 + 'w'
//                 } else if (value > 0) {
//                     return (value / 1000).toFixed(1) + 'k'
//                 } else {
//                     return value
//                 }
//             }
//         }
//     },
//     dataZoom: [
//         {
//             type: 'inside'
//         }
//     ],
//     series: [
//         {
//             // data: [3303, 794, 1296, 1456, 1577, 1588, 1450, 1747, 1515, 2153, 1776, 1663],
//             type: 'line',
//             smooth: true
//         }
//     ]
// });
//
// var response = request({url: '/v1/data/proportionOfChineseAndForeignAuthors'})
// response.then((res) => {
//     var xAxisLabel = []
//     for (const month in res['xAxis']) {
//         xAxisLabel.push(`${month}月`)
//     }
//     proportionOfChineseAndForeignAuthors.setOption({
//         xAxis: [{
//             data: xAxisLabel,
//         }],
//         series: [{
//             data: res['yAxis']
//         }]
//     });
// })
//
// window.addEventListener("resize", function () {
//     everyMonthPublishNum.resize();
// });