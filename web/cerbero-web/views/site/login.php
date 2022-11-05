<?php

use yii\helpers\Html;
?>
<div class="col-5 container">
    <div class="card">
        <div class="card-body login-card-body">
            <h1>
                <p class="login-box-msg">
                    Inicie a seção
                </p>
            </h1>
            <?php $form = \yii\bootstrap4\ActiveForm::begin(['id' => 'login-form']) ?>


            <?= $form->field($model, 'username', [
                'options' => ['class' => 'form-group has-feedback'],
                'inputTemplate' => '{input}<div class="input-group-append"><div class="input-group-text"><span class="fas fa-envelope"></span></div></div>',
                'template' => '{beginWrapper}{input}{error}{endWrapper}',
                'wrapperOptions' => ['class' => 'input-group mb-3']
            ])
                ->label(false)
                ->textInput(['placeholder' => $model->getAttributeLabel('username')]) ?>



            <?= $form->field($model, 'password', [
                'options' => ['class' => 'form-group has-feedback'],
                'inputTemplate' => '{input}<div class="input-group-append"><div class="input-group-text"><span class="fas fa-lock"></span></div></div>',
                'template' => '{beginWrapper}{input}{error}{endWrapper}',
                'wrapperOptions' => ['class' => 'input-group mb-3']
            ])
                ->label(false)
                ->passwordInput(['placeholder' => $model->getAttributeLabel('password')]) ?>




            <?= Html::submitButton('Acessar', ['class' => 'btn btn-primary btn-block']) ?>


            <?php \yii\bootstrap4\ActiveForm::end(); ?>

            <!-- /.social-auth-links -->
        </div>
        <!-- /.login-card-body -->
    </div>

</div>