(async () => {
    var res = await request({ url: '/v1/data/commentCategories' })
    var data = []
    for (const key in res) {
        data.push({
            'name': key,
            'value': res[key]
        })
    }
    // 实例化对象
    const commentCategories = echarts.init(document.getElementById('commentCategories'), 'dark');
    // 指定配置和数据
    commentCategories.setOption({
        backgroundColor: 'transparent',
        tooltip: {
            trigger: 'item',
        },
        grid: {
            left: '3%',
            right: '2%',
            bottom: '2%',
            top: '2%',
            containLabel: true,
            // backgroundColor: #fff
        },
        series: [
            {
                type: 'pie',
                radius: [30, 100],
                avoidLabelOverlap: false,
                center: ['50%', '50%'],
                // roseType: 'area',
                itemStyle: {
                    borderRadius: 10,
                    // borderColor: '#fff',
                    borderWidth: 0
                },
                label: {
                    show: true,
                    position: 'inside',
                },
                labelLine: {
                    show: true
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '15',
                        color: '#fff',
                    }
                },
                // data: [
                //     {value: 241, name: '差强人意'},
                //     {value: 348, name: '瑕不掩瑜'},
                //     {value: 15, name: '一致好评'},
                //     {value: 8, name: '一塌糊涂'},
                //     {value: 3, name: '味同嚼蜡'},
                // ]
                data: data
            }
        ]
    });
    // window.addEventListener("resize", function () {
    //     commentCategories.resize();
    // });
})()