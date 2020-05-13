<template>
    <div>
        <NavMenu></NavMenu>
        <Breadcrumb id="Breadcrumb"></Breadcrumb>
        <Avatar id="Avatar"></Avatar>
        <el-divider id="divider1"></el-divider>
        <personal></personal>
    </div>
</template>

<script>
    import Breadcrumb from '../../components/Breadcrumb.vue'
    import Personal from '../../components/Person/PersonalInfo.vue'
    import NavMenu from '../../components/NavMenu.vue'
    import Avatar from "../../components/Avatar";

    export default{
        components: {
            Breadcrumb,
            Personal,
            NavMenu,
            Avatar
        },
    }

</script>

<style scoped>
    #Breadcrumb{
        margin-top: 20px;
        margin-left: 300px;
    }
    #divider1{
        width: 86%;
        margin-top: 11px;
        margin-left: 244px;
    }
    #Avatar {
        margin-left: 93%;
        margin-top: -27px;
    }
</style>