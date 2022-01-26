(async () => {
    var res = await request({ url: '/v1/data/proportionOfChineseAndForeignAuthors' })
    var data = []
    for (const key in res) {
        data.push({
            'name': key,
            'value': res[key]
        })
    }
    // 实例化对象
    const proportionOfChineseAndForeignAuthors = echarts.init(document.getElementById('proportionOfChineseAndForeignAuthors'));
    // 指定配置和数据
    proportionOfChineseAndForeignAuthors.setOption({
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
        legend: {
            top: 0,
            itemWidth: 30,   // 设置图例图形的宽
            itemHeight: 15,  // 设置图例图形的高
            textStyle: {
                color: '#fff',  // 图例文字颜色
                fontSize: 14,
            },
            // itemGap: 30,
        },
        series: [
            {
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 0
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '15',
                        color: '#fff',
                    }
                },
                labelLine: {
                    show: false
                },
                data: data
                // data: [
                //     {value: 15078, name: '中文书籍'},
                //     {value: 12956, name: '外文书籍'}
                // ]
            }
        ]
    });
})()