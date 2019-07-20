<h2>About the study</h2>
mPower research study was developed by Sage Bionetworks (non-profit) to measure the symptoms, day to day changes, and long-term changes in people with Parkinson’s Disease (PD).

<h2>How does the study work?</h2>
1. Answer questions to determine if you are eligible for this study 
2. Complete the informed consent process & download the app
3. Complete a one-time health survey
4. Complete short physical and cognitive activities 
5. Track your symptoms, triggers, and medications

<h2>How long does it last?</h2>
We will ask you to participate for 2 weeks every three months. We would like you to participate for 2 years, but you can participate as long as you like.

<h2>What are the benefits and risks?</h2>
You may not directly benefit from taking part but seeing trends in your data may be interesting to you. You may help researchers better understand PD.

The main risk is to your privacy by an accidental release of your data. You may find some of the activities tiring and seeing your data may be stressful.



<template>
  <div class="docked-layout">
    <nav class="basic">
      <div>About mPower</div>
    </nav>
    <section v-freeze>
      <div class="container">
        <div class="screen" v-show="step === 1">
          <div class="panel">
            <BridgeImage src="/static/images/about%20the%20study.svg"/>

            <h3>About the study</h3>
            <p>mPower research study was developed by Sage Bionetworks (non-profit) to measure the symptoms, day to day changes, and long-term changes in people with Parkinson’s Disease (PD). </p>
            <p><a href="" @click.prevent="learnMore">Learn more</a></p>

            <DocumentViewer ref="consentViewer">
              <ConsentContent/>
            </DocumentViewer>

          </div>
        </div>
        <div class="screen" v-show="step === 2">
          <div class="panel">
            <BridgeImage src="/static/images/procedures%20activities.svg"/>
            <h3>How does the study work?</h3>
            <p>
              1. Answer questions to determine if you are eligible for this study <br>
              2. Complete the informed consent process & download the app<br>
              3. Complete a one-time health survey<br>
              4. Complete short physical and cognitive activities <br>
              5. Track your symptoms, triggers, and medications
            </p>
          </div>
        </div>
        <div class="screen" v-show="step === 3">
          <div class="panel">
            <BridgeImage src="/static/images/how%20long%20does%20it%20last.svg"/>
            <h3>How long does it last?</h3>
            <p>We will ask you to participate for 2 weeks every three months. We would like you to participate for 2 years, but you can participate as long as you like.</p>
          </div>
        </div>
        <div class="screen" v-show="step === 4">
          <div class="panel">
            <BridgeImage src="/static/images/benefits%20and%20risks.svg"/>
            <h3>What are the benefits and risks?</h3>
            <p>You may not directly benefit from taking part but seeing trends in your data may be interesting to you. You may help researchers better understand PD.</p>

            <p>The main risk is to your privacy by an accidental release of your data. You may find some of the activities tiring and seeing your data may be stressful.</p>
          </div>
        </div>
      </div>
    </section>
    <div class="buttons" v-freeze>
      <button @click="doBack" :disabled="this.step === 1">Back</button>
      <button @click="doNext">{{nextName}}</button>
    </div>
  </div>
</template>
