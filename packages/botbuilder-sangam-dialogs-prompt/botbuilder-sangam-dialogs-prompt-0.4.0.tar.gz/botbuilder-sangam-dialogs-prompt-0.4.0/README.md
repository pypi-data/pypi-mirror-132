# Dialog Prompts

This package contains additional Inputs , beyond those offered out of the box by the Bot Framework SDK. 

## AdaptiveCardPrompt

The AdaptiveCardPrompt is use in waterfallDialog to receive adaptive card event.

## Installing

    pip install botbuilder-sangam-dialogs-prompt

## Usage
You can then import required types, for example:

```python
   
   from botbuilder.sangam.dialogs.prompt.adaptive import AdaptiveCardPrompt
   
   self.dialog_set.add(AdaptiveCardPrompt("adaptive_prompt"))
   
```

Then, you can call the bot by specifying your PromptOptions and calling PromptAsync.

```python           
   
   async def adaptive_card(self,waterfall_step:WaterfallStepContext):
      
      # card = pass adaptive card information
  
        message = Activity(
            text="Here is an Adaptive Card:",
            type=ActivityTypes.message,
            attachments=[CardFactory.adaptive_card(card)],
        )

        prompt_options = PromptOptions()
        prompt_options.prompt = message
        prompt_options.Type = ActivityTypes.message

        return await waterfall_step.prompt("adaptive_prompt",prompt_options)   
   
```

