<template>
    <div class="container">
        <div class="jumbotron mt-5">
            <div class="col-sm-8 mx-auto">
                <h1 class="text-center">Dashboard</h1>
            </div>
            <table class="table col-md-6 mx-auto">
                <tbody>
                <tr>
                    <td class="text-center">{{msg}}</td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'coming soon...'
    }
  }
}

</script>
