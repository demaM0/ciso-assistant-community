<script lang="ts">
	import ModelForm from '$lib/components/Forms/ModelForm.svelte';
	import { SSOSettingsSchema, GeneralSettingsSchema, FeatureFlagsSchema } from '$lib/utils/schemas';
	import { m } from '$paraglide/messages';
	import { TabGroup, Tab } from '@skeletonlabs/skeleton';

	let tabSet = 0;

	export let data;
</script>

<TabGroup active="bg-primary-100 text-primary-800 border-b border-primary-800">
	<Tab bind:group={tabSet} name="instanceSettings" value={0}
		><i class="fa-solid fa-globe"></i> {m.general()}</Tab
	>
	<Tab bind:group={tabSet} name="ssoSettings" value={1}><i class="fa-solid fa-key" /> {m.sso()}</Tab
	>
	<Tab bind:group={tabSet} name="featureFlags" value={2}
		><i class="fa-solid fa-flag" /> {m.featureFlags()}</Tab
	>
</TabGroup>
{#if tabSet === 0}
	<div>
		<span class="text-gray-500">{m.generalSettingsDescription()}</span>
		<ModelForm
			form={data.generalSettingForm}
			schema={GeneralSettingsSchema}
			model={data.generalSettingModel}
			cancelButton={false}
			action="?/general"
		/>
	</div>
{:else if tabSet === 1}
	<div>
		<span class="text-gray-500">{m.ssoSettingsDescription()}</span>
		<ModelForm
			form={data.ssoForm}
			schema={SSOSettingsSchema}
			model={data.ssoModel}
			cancelButton={false}
			action="?/sso"
		/>
	</div>
{:else if tabSet === 2}
	<div>
		<span class="text-gray-500">{m.configureFeatureFlags()}</span>
		<ModelForm
			form={data.featureFlagForm}
			schema={FeatureFlagsSchema}
			model={data.featureFlagModel}
			cancelButton={false}
			action="?/featureFlags"
		/>
	</div>
{/if}
