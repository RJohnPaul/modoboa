<template>
<validation-observer ref="observer">
  <validation-provider
    vid="alias"
    v-slot="{ errors }"
    >
    <email-field
      ref="aliasField"
      v-model="currentAlias"
      :placeholder="'Start typing a name here...'|translate"
      @domain-selected="addAlias"
      :hint="'Alias(es) of this mailbox. To create a catchall alias, just enter the domain name (@domain.tld).'|translate"
      persistent-hint
      :error-messages="errors"
      />
  </validation-provider>
  <v-chip
    v-for="(alias, index) in form.aliases"
    :key="index"
    class="mr-2 mt-2"
    close
    @click:close="removeAlias(index)"
    >
    {{ alias }}
  </v-chip>
</validation-observer>
</template>

<script>
import accounts from '@/api/accounts'
import EmailField from '@/components/tools/EmailField'

export default {
  props: ['value'],
  components: {
    EmailField
  },
  data () {
    return {
      form: {
        mailbox: {},
        aliases: []
      },
      currentAlias: ''
    }
  },
  methods: {
    reset () {
      this.currentAlias = ''
      this.form.aliases = []
    },
    update () {
      this.$emit('input', this.form)
    },
    async addAlias () {
      try {
        await accounts.validate({ aliases: [this.currentAlias], mailbox: this.form.mailbox })
        this.form.aliases.push(this.currentAlias)
        this.$refs.aliasField.reset()
      } catch (error) {
        let errorMsg = null
        if (error.response.data.aliases) {
          errorMsg = error.response.data.aliases
        } else if (error.response.data.non_field_errors) {
          errorMsg = error.response.data.non_field_errors
        }
        this.$refs.observer.setErrors({ alias: errorMsg })
      }
    },
    removeAlias (index) {
      this.form.aliases.splice(index, 1)
      this.update()
    }
  },
  mounted () {
    this.form = { ...this.value }
  },
  watch: {
    value: {
      handler (newValue) {
        this.form = { ...newValue }
      },
      deep: true
    }
  }
}
</script>
