<template>
  <div id="app">
    <button v-on:click="catchData">点我</button>
    <ul>
      <li v-for="item in items" v-bind:key="item.hello">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: 'App',
        data () {
            return {
                items:[{hello:"vue"}]
            }
        },
        methods: {
            catchData () {
                // 为了在内部函数能使用外部函数的this对象
                var self = this;
                this.$axios.get("http://127.0.0.1:5000/api/sensors")
                    .then(res => {
                        console.log(res);
                        console.log(res.data);
                        self.items.push(res.data);
                    });
            }
        }
    }
</script>
